# kbm_app/kbm_core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Tambahkan 'reverse' untuk mendapatkan URL by name
from datetime import datetime
from .models import Kelas, Guru, Tahunajaran
from .forms import KelasForm
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

    context = {
        'kelas': kelas, # Mengirim objek kelas ke template
        'judul_halaman': f'Detail Kelas: {kelas.namakelas}' # Judul halaman dinamis
    }
    return render(request, 'kbm_core/detail_kelas.html', context) # Menggunakan template baru