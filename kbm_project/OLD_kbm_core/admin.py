#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Absensipd, Catatankegiatanguru, Elemencapaian, ElemencapaianHasRpp, Guru, GuruHasMatapelajaran, GuruHasTugastambahan, Jeniskegiatanguru, Kegiatankbm, Kelas, Masatugastambahan, Matapelajaran, Pesertadidik, Riwayatkelaspd, Rpp, Sumberrpp, Tahunajaran, Tugastambahan # Impor semua model 

# Register your models here.
admin.site.register(Absensipd)
admin.site.register(Catatankegiatanguru)
admin.site.register(Elemencapaian)
admin.site.register(ElemencapaianHasRpp)
admin.site.register(Guru)
admin.site.register(GuruHasMatapelajaran)
admin.site.register(GuruHasTugastambahan)
admin.site.register(Jeniskegiatanguru)
admin.site.register(Kegiatankbm)
admin.site.register(Kelas)
admin.site.register(Masatugastambahan)
admin.site.register(Matapelajaran)
admin.site.register(Pesertadidik)
admin.site.register(Riwayatkelaspd)
admin.site.register(Rpp)
admin.site.register(Sumberrpp)
admin.site.register(Tahunajaran)
admin.site.register(Tugastambahan)
# Daftarkan semua model KBM Anda di sini