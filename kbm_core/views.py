# kbm_app/kbm_core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Tambahkan 'reverse' untuk mendapatkan URL by name
from datetime import datetime
from .models import Kelas, Riwayatkelaspd, Guru, Tahunajaran, Pesertadidik
from .forms import KelasForm, GuruForm, SiswaForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time,
    }
    return render(request, 'kbm_core/home.html', context)

@login_required
def about(request):
    return render(request, 'kbm_core/about.html')

@login_required
def daftar_kelas(request):
    kelas_list = Kelas.objects.all()
    context = {
        'kelas_list': kelas_list
    }
    return render(request, 'kbm_core/daftar_kelas.html', context)

@login_required
def tambah_kelas(request):
    if request.method == 'POST':
        form = KelasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_kelas')
    else:
        form = KelasForm()

    context = {
        'form': form,
        'judul_halaman': 'Tambah Kelas Baru'
    }
    return render(request, 'kbm_core/tambah_kelas.html', context)

@login_required
def edit_kelas(request, id_kelas):
    kelas = get_object_or_404(Kelas, idkelas=id_kelas)

    if request.method == 'POST':
        form = KelasForm(request.POST, instance=kelas)
        if form.is_valid():
            form.save()
            return redirect('daftar_kelas')
    else:
        form = KelasForm(instance=kelas)

    context = {
        'form': form,
        'judul_halaman': f'Edit Kelas: {kelas.namakelas}'
    }
    return render(request, 'kbm_core/tambah_kelas.html', context)

# Tambahkan fungsi view baru ini untuk menghapus kelas
@login_required
def hapus_kelas(request, id_kelas):
    kelas = get_object_or_404(Kelas, idkelas=id_kelas)
    if request.method == 'POST':
        kelas.delete()
        return redirect('daftar_kelas')
    else:
        # Mengirimkan konteks untuk template konfirmasi umum
        context = {
            'object_to_delete': kelas, # Objek Kelas yang akan dihapus (akan menggunakan __str__)
            'delete_url': reverse('hapus_kelas', kwargs={'id_kelas': kelas.idkelas}), # URL POST untuk hapus
            'cancel_url': reverse('daftar_kelas'), # URL untuk membatalkan dan kembali
        }
        return render(request, 'kbm_core/konfirmasi_hapus.html', context) # Menggunakan template umum

# Tambahkan fungsi view baru ini untuk detail kelas
@login_required
def detail_kelas(request, id_kelas):
    # Mengambil objek Kelas berdasarkan id_kelas, atau mengembalikan 404 jika tidak ditemukan
    kelas = get_object_or_404(Kelas, idkelas=id_kelas)

    try:
        tahun_ajaran_aktif = Tahunajaran.objects.get(isactive=1)
    except Tahunajaran.DoesNotExist:
        tahun_ajaran_aktif = None
    except Tahunajaran.MultipleObjectsReturned:
        # Tangani jika ada lebih dari satu tahun ajaran aktif, mungkin ambil yang terbaru
        tahun_ajaran_aktif = Tahunajaran.objects.filter(isactive=1).order_by('-tglmulai').first()

    peserta_didik_list = []
    if tahun_ajaran_aktif:
        peserta_didik_di_kelas_riwayat = Riwayatkelaspd.objects.filter(
            kelas_idkelas=kelas,
            tahunajaran_idtahunajaran=tahun_ajaran_aktif
        ).select_related('pesertadidik_idpesertadidik')

        peserta_didik_list = [
            riwayat.pesertadidik_idpesertadidik for riwayat in peserta_didik_di_kelas_riwayat
        ]

    context = {
        'kelas': kelas,
        'peserta_didik_list': peserta_didik_list
    }
    return render(request, 'kbm_core/detail_kelas.html', context)
    # context = {
    #    'kelas': kelas, # Mengirim objek kelas ke template
    #    'judul_halaman': f'Detail Kelas: {kelas.namakelas}' # Judul halaman dinamis
    #}
    #return render(request, 'kbm_core/detail_kelas.html', context) # Menggunakan template baru

    # ==== VIEWS UNTUK MANAJEMEN GURU ====

# fungsi daftar guru ada nomor urut dan bisa di sort

@login_required
def daftar_guru(request):
    # Ambil parameter sorting dari URL, jika tidak ada, gunakan default
    sort_by = request.GET.get('sort', 'nama_lengkap') # Default sort by nama_lengkap
    direction = request.GET.get('direction', 'asc')   # Default direction ascending

    # Whitelist untuk keamanan: hanya field ini yang boleh di-sort
    allowed_sort_fields = ['nama_lengkap', 'nama_instansi']
    if sort_by not in allowed_sort_fields:
        sort_by = 'nama_lengkap' # Kembali ke default jika field tidak diizinkan

    # Tentukan arah pengurutan
    if direction == 'desc':
        order_by_field = f'-{sort_by}'
        next_direction = 'asc'
    else:
        order_by_field = sort_by
        next_direction = 'desc'

    # Ambil data dari database dan urutkan
    guru_list = Guru.objects.all().order_by(order_by_field)

    context = {
        'guru_list': guru_list,
        'sort_by': sort_by,
        'direction': direction,
        'next_direction': next_direction
    }
    return render(request, 'kbm_core/daftar_guru.html', context)

@login_required
def detail_guru(request, id_guru):
    guru = get_object_or_404(Guru, idguru=id_guru)
    context = {
        'guru': guru
    }
    return render(request, 'kbm_core/detail_guru.html', context)

# C:\app\kbm_app\kbm_core\views.py

@login_required
def tambah_guru(request):
    if request.method == 'POST':
        # 'request.FILES' penting untuk menangani upload file
        form = GuruForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Menyimpan data baru, termasuk foto
            # messages.success(request, 'Data guru berhasil ditambahkan!') # Opsional: untuk notifikasi
            return redirect('daftar_guru')
    else:
        form = GuruForm() # Tampilkan form kosong

    context = {
        'form': form,
        'judul_halaman': 'Tambah Guru Baru'
    }
    return render(request, 'kbm_core/form_guru.html', context)

@login_required
def edit_guru(request, id_guru):
    guru = get_object_or_404(Guru, idguru=id_guru)
    if request.method == 'POST':
        # 'instance=guru' untuk memberitahu form bahwa kita sedang mengedit data yang sudah ada
        form = GuruForm(request.POST, request.FILES, instance=guru)
        if form.is_valid():
            form.save() # Memperbarui data yang ada
            # messages.success(request, 'Data guru berhasil diperbarui!') # Opsional
            return redirect('daftar_guru')
    else:
        form = GuruForm(instance=guru) # Tampilkan form dengan data yang sudah ada

    context = {
        'form': form,
        'judul_halaman': f'Edit Data Guru: {guru.nama_lengkap}'
    }
    return render(request, 'kbm_core/form_guru.html', context)

@login_required
def hapus_guru(request, id_guru):
    guru = get_object_or_404(Guru, idguru=id_guru)
    if request.method == 'POST':
        guru.delete()
        return redirect('daftar_guru')
    
    context = {
        'object_to_delete': guru,
        'delete_url': reverse('hapus_guru', kwargs={'id_guru': guru.idguru}),
        'cancel_url': reverse('daftar_guru')
    }
    return render(request, 'kbm_core/konfirmasi_hapus.html', context)

# ==== VIEWS UNTUK MANAJEMEN SISWA ====

@login_required
def daftar_siswa(request):
    sort_by = request.GET.get('sort', 'namalengkappd')
    direction = request.GET.get('direction', 'asc')

    allowed_sort_fields = ['namalengkappd', 'nis', 'nisn']
    if sort_by not in allowed_sort_fields:
        sort_by = 'namalengkappd'

    order_by_field = f'-{sort_by}' if direction == 'desc' else sort_by
    siswa_list = Pesertadidik.objects.all().order_by(order_by_field)

    context = {
        'siswa_list': siswa_list,
        'sort_by': sort_by,
        'direction': direction,
    }
    return render(request, 'kbm_core/daftar_siswa.html', context)

@login_required
def detail_siswa(request, id_siswa):
    siswa = get_object_or_404(Pesertadidik, idpesertadidik=id_siswa)
    # Ambil data riwayat kelas untuk siswa ini
    riwayat_kelas = Riwayatkelaspd.objects.filter(pesertadidik_idpesertadidik=siswa).order_by('-tahunajaran_idtahunajaran')
    context = {
        'siswa': siswa,
        'riwayat_kelas': riwayat_kelas
    }
    return render(request, 'kbm_core/detail_siswa.html', context)

@login_required
def tambah_siswa(request):
    if request.method == 'POST':
        form = SiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_siswa')
    else:
        form = SiswaForm()
    context = {
        'form': form,
        'judul_halaman': 'Tambah Siswa Baru'
    }
    return render(request, 'kbm_core/form_siswa.html', context)

@login_required
def edit_siswa(request, id_siswa):
    siswa = get_object_or_404(Pesertadidik, idpesertadidik=id_siswa)
    if request.method == 'POST':
        form = SiswaForm(request.POST, instance=siswa)
        if form.is_valid():
            form.save()
            return redirect('daftar_siswa')
    else:
        form = SiswaForm(instance=siswa)
    context = {
        'form': form,
        'judul_halaman': f'Edit Data Siswa: {siswa.namalengkappd}'
    }
    return render(request, 'kbm_core/form_siswa.html', context)

@login_required
def hapus_siswa(request, id_siswa):
    siswa = get_object_or_404(Pesertadidik, idpesertadidik=id_siswa)
    if request.method == 'POST':
        siswa.delete()
        return redirect('daftar_siswa')
    context = {
        'object_to_delete': siswa,
        'delete_url': reverse('hapus_siswa', kwargs={'id_siswa': siswa.idpesertadidik}),
        'cancel_url': reverse('daftar_siswa')
    }
    return render(request, 'kbm_core/konfirmasi_hapus.html', context)