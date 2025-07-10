# C:\app\kbm_app\kbm_core\forms.py

from django import forms
from .models import Kelas, Guru, Tahunajaran, Pesertadidik

class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        # Tentukan field yang ingin ditampilkan di form
        fields = ['namakelas', 'tingkat', 'jurusan', 'guru_walikelas', 'tahunajaran']

        # Tambahkan label kustom yang lebih ramah pengguna
        labels = {
            'namakelas': 'Nama Kelas',
            'tingkat': 'Tingkat/Jenjang',
            'jurusan': 'Jurusan/Program',
            'guru_walikelas': 'Wali Kelas',
            'tahunajaran': 'Tahun Pelajaran',
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
        self.fields['guruwalikelas'].empty_label = "--- Pilih Wali Kelas ---"
        self.fields['guruwalikelas'].required = False
        self.fields['tahunajaran'].empty_label = "--- Pilih Tahun Pelajaran ---"
        # Tambahan: Jika 'lembaga' dan 'guru_pembuat' adalah field yang juga ingin dipilih di form
        self.fields['lembaga'].empty_label = "--- Pilih Lembaga ---"
        self.fields['guru_pembuat'].empty_label = "--- Pilih Guru Pembuat ---"

# UNTUK FORM EDIT/TAMBAH GURU

class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        # Tentukan semua field dari model Guru yang ingin Anda sertakan di form
        # Kita sengaja tidak menyertakan 'pwd' karena manajemen password sebaiknya ditangani terpisah
        fields = [
            'nama_lengkap', 'nip', 'nuptk', 'status'
            
        ]

        # Berikan label yang lebih mudah dibaca untuk setiap field
        labels = {
            'nama_lengkap': 'Nama Lengkap',
            'nip': 'NIP',
            'nuptk': 'NUPTK',
            'status': 'Status Kepegawaian'
            #'username': 'Username'
            
        }

        # Terapkan kelas Bootstrap ke setiap field menggunakan widgets
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'nuptk': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            #'username': forms.TextInput(attrs={'class': 'form-control'}),
            #'foto': forms.FileInput(attrs={'class': 'form-control'}), # Widget untuk upload file
            #'nama_instansi': forms.TextInput(attrs={'class': 'form-control'}),
            #'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), # Textarea untuk alamat
        }

 # ==== FORM UNTUK SISWA (PESERTA DIDIK) ====
 
class SiswaForm(forms.ModelForm):
    # Definisikan pilihan untuk field gender
    GENDER_CHOICES = [
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    ]

    # Override field gender untuk menggunakan pilihan di atas
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    # Override field tanggal lahir untuk menggunakan input tipe date
    tgllahir = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Tanggal Lahir'
    )

    class Meta:
        model = Pesertadidik
        # 1. Tambahkan 'jenis_siswa' ke dalam daftar fields
        fields = ['namalengkappd', 'nis', 'nisn', 'gender', 'tgllahir', 'jenis_siswa', 'is_berkebutuhan_khusus']

        labels = {
            'namalengkappd': 'Nama Lengkap Peserta Didik',
            'nis': 'NIS (Nomor Induk Siswa)',
            'nisn': 'NISN (Nomor Induk Siswa Nasional)',
            # 2. Tambahkan label untuk field baru
            'jenis_siswa': 'Jenis Siswa',
            # 2. Tambahkan label untuk field checkbox
            'is_berkebutuhan_khusus': 'Berkebutuhan Khusus?',
        }
        widgets = {
            'namalengkappd': forms.TextInput(attrs={'class': 'form-control'}),
            'nis': forms.TextInput(attrs={'class': 'form-control'}),
            'nisn': forms.TextInput(attrs={'class': 'form-control'}),
            # 3. Tambahkan widget agar tampilannya bagus (dropdown)
            'jenis_siswa': forms.Select(attrs={'class': 'form-select'}),
            # 3. Tambahkan widget agar checkbox sesuai gaya Bootstrap
            'is_berkebutuhan_khusus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }       