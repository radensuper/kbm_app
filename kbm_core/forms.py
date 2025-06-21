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