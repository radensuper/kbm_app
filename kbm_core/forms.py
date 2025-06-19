# kbm_app/kbm_core/forms.py
from django import forms
from .models import Kelas, Guru, Tahunajaran # Import model yang relevan

class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        # fields = '__all__' # Ini akan menyertakan semua bidang dari model Kelas
        # Atau, tentukan bidang mana saja yang ingin Anda tampilkan:
        fields = ['namakelas', 'tingkat', 'jurusan', 'guru_idguru', 'tahunajaran_idtahunajaran']

        # Optional: Menyesuaikan label untuk tampilan yang lebih baik di form
        labels = {
            'namakelas': 'Nama Kelas',
            'tingkat': 'Tingkat/Jenjang',
            'jurusan': 'Jurusan/Program',
            'guru_idguru': 'Wali Kelas', # Django akan otomatis mengenali ini adalah FK ke Guru
            'tahunajaran_idtahunajaran': 'Tahun Pelajaran',
        }

        # Optional: Menyesuaikan widget jika diperlukan (misalnya untuk TextField)
        widgets = {
            # 'deskripsi': forms.Textarea(attrs={'rows': 4}),
        }