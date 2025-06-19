# kbm_app/kbm_core/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView # <--- PASTIKAN BARIS INI ADA!

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kelas/', views.daftar_kelas, name='daftar_kelas'),
    path('kelas/tambah/', views.tambah_kelas, name='tambah_kelas'),
    path('kelas/<int:id_kelas>/edit/', views.edit_kelas, name='edit_kelas'),
    path('kelas/<int:id_kelas>/hapus/', views.hapus_kelas, name='hapus_kelas'),
    path('kelas/<int:id_kelas>/', views.detail_kelas, name='detail_kelas'), # TAMBAHKAN BARIS INI
    path('login/', LoginView.as_view(template_name='kbm_core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]