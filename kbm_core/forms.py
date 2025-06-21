# C:\app\kbm_app\kbm_core\forms.py

from django import forms
from .models import Kelas, Guru, Tahunajaran

class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        # Tentukan field yang ingin ditampilkan di form
        fields = ['namakelas', 'tingkat', 'jurusan', 'guru_idguru', 'tahunajaran_idtahunajaran']

        # Tambahkan label kustom yang lebih ramah pengguna
        labels = {
            'namakelas': 'Nama Kelas',
            'tingkat': 'Tingkat/Jenjang',
            'jurusan': 'Jurusan/Program',
            'guru_idguru': 'Wali Kelas',
            'tahunajaran_idtahunajaran': 'Tahun Pelajaran',
        }

        # Di sinilah keajaibannya: kita definisikan widget untuk setiap field
        widgets = {
            'namakelas': forms.TextInput(
                attrs={
                    'class': 'form-control', # Kelas untuk input teks
                    'placeholder': 'Contoh: 10 IPA 1'
                }
            ),
            'tingkat': forms.Select(
                attrs={
                    'class': 'form-select' # Kelas untuk dropdown/select
                }
            ),
            'jurusan': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'guru_idguru': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'tahunajaran_idtahunajaran': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    # Menambahkan field kosong pada pilihan dropdown
    def __init__(self, *args, **kwargs):
        super(KelasForm, self).__init__(*args, **kwargs)
        # Menjadikan field Wali Kelas tidak wajib diisi
        self.fields['guru_idguru'].empty_label = "--- Pilih Wali Kelas ---"
        self.fields['guru_idguru'].required = False
        self.fields['tahunajaran_idtahunajaran'].empty_label = "--- Pilih Tahun Pelajaran ---"

# UNTUK FORM EDIT/TAMBAH GURU

class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        # Tentukan semua field dari model Guru yang ingin Anda sertakan di form
        # Kita sengaja tidak menyertakan 'pwd' karena manajemen password sebaiknya ditangani terpisah
        fields = [
            'nama_lengkap', 'nip', 'nuptk', 'status', 'username', 
            'foto', 'nama_instansi', 'alamat'
        ]

        # Berikan label yang lebih mudah dibaca untuk setiap field
        labels = {
            'nama_lengkap': 'Nama Lengkap',
            'nip': 'NIP',
            'nuptk': 'NUPTK',
            'status': 'Status Kepegawaian',
            'username': 'Username',
            'foto': 'Upload Foto Profil',
            'nama_instansi': 'Nama Instansi (isikan nama resmi di Laporan/RPP/LCK)',
            'alamat': 'Alamat Instansi'
        }

        # Terapkan kelas Bootstrap ke setiap field menggunakan widgets
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'nuptk': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}), # Widget untuk upload file
            'nama_instansi': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), # Textarea untuk alamat
        }