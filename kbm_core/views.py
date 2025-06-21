# kbm_app/kbm_core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Tambahkan 'reverse' untuk mendapatkan URL by name
from datetime import datetime
from .models import Kelas, Riwayatkelaspd, Guru, Tahunajaran
from .forms import KelasForm, GuruForm
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

@login_required
def daftar_guru(request):
    guru_list = Guru.objects.all()
    context = {
        'guru_list': guru_list
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