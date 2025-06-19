# kbm_app/kbm_core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Kelas, Guru, Tahunajaran
from .forms import KelasForm

def home(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time,
    }
    return render(request, 'kbm_core/home.html', context)

def about(request):
    return render(request, 'kbm_core/about.html')

def daftar_kelas(request):
    kelas_list = Kelas.objects.all()
    context = {
        'kelas_list': kelas_list
    }
    return render(request, 'kbm_core/daftar_kelas.html', context)

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
def hapus_kelas(request, id_kelas):
    kelas = get_object_or_404(Kelas, idkelas=id_kelas)
    if request.method == 'POST':
        kelas.delete() # Menghapus objek dari database
        return redirect('daftar_kelas') # Redirect kembali ke daftar kelas
    # Jika bukan POST (misal GET), kita mungkin ingin menampilkan halaman konfirmasi.
    # Untuk kesederhanaan, kita langsung arahkan ke daftar kelas jika diakses via GET tanpa POST.
    # Atau, Anda bisa membuat template konfirmasi hapus terpisah jika diperlukan.
    return render(request, 'kbm_core/konfirmasi_hapus_kelas.html', {'kelas': kelas})