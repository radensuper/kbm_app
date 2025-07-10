# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from PIL import Image # <--- Import Pillow
from django.contrib.auth.models import AbstractUser

# Definisi Choices untuk Tingkat
TINGKAT_CHOICES = [
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
]

# Definisi Choices untuk Jurusan
JURUSAN_CHOICES = [
    ('UMUM', 'Umum'),
    ('IPA', 'IPA'),
    ('IPS', 'IPS'),
    ('BAHASA', 'Bahasa'),
    ('LAINNYA', 'Lainnya'), # Menambahkan pilihan 'Lainnya'
]

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

#1
class LembagaPendidikan(models.Model): # Pindahkan atau pastikan ini didefinisikan sebelum AppUser
    idlembaga = models.AutoField(db_column='idlembaga', primary_key=True)
    nama_lembaga = models.CharField(max_length=255, unique=True)
    alamat_lembaga = models.TextField(blank=True, null=True)
    telepon_lembaga = models.CharField(max_length=50, blank=True, null=True)
    email_lembaga = models.CharField(max_length=100, blank=True, null=True)
    npsn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    kepala_lembaga = models.CharField(max_length=255, blank=True, null=True)
    nipnuptk_kepala = models.CharField(max_length=45, unique=True, blank=True, null=True)
    logo_lembaga = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'lembaga_pendidikan'

    def __str__(self):
        return self.nama_lembaga

#2
# Definisi Choices untuk Role AppUser
ROLE_CHOICES = [
    ('super_admin', 'Super Admin'),
    ('lembaga_admin', 'Lembaga Admin'),
    ('guru_individual', 'Guru Individual'),
    ('guru_lembaga', 'Guru Lembaga'),
]

class AppUser(AbstractUser):
    # Username, password, email sudah ada di AbstractUser
    # pwd = models.CharField(max_length=255) # Jangan gunakan ini jika pakai AbstractUser, password sudah dikelola
    # email = models.CharField(max_length=255, unique=True, blank=True, null=True) # Ini sudah ada di AbstractUser, pastikan unique=True
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='guru_individual', help_text='Peran pengguna dalam sistem')
    lembaga = models.ForeignKey(LembagaPendidikan, on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True, help_text='Hanya diisi jika role adalah lembaga_admin atau guru_lembaga, menandakan afiliasi admin/guru dengan lembaga tertentu')
    active = models.BooleanField(default=True) # is_active dari AbstractUser bisa digunakan
    profile_foto = models.CharField(max_length=255, blank=True, null=True) # Atau models.ImageField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta(AbstractUser.Meta):
        db_table = 'app_users' 
   
#3
class Guru(models.Model):
    idguru = models.AutoField(primary_key=True)
    # user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, db_column='user_iduser') # jika pakai AuthUser bawaan Django
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, db_column='user_iduser')
    nama_lengkap = models.CharField(max_length=255)
    nip = models.CharField(max_length=20, blank=True, null=True)
    nuptk = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, db_comment='Status kepegawaian/mengajar guru (e.g., Aktif, Nonaktif, Cuti)')
    # foto = models.ImageField(upload_to='guru_photos/', blank=True, null=True) # ini harusnya di AppUser.profile_foto
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        db_table = 'guru'

    def __str__(self):
        return self.nama_lengkap

    # Metode save kustom untuk foto harusnya ada di model user yang memiliki profile_foto
    # atau Anda harus memindahkan foto ke model Guru jika memang ingin menyimpan foto profil di Guru.
    # Jika Anda ingin menyimpan foto di Guru, pastikan field foto juga ada di skema SQL Guru.
    # Saat ini di skema SQL Guru tidak ada field foto.

#4
class Tahunajaran(models.Model):
    idtahunajaran = models.AutoField(db_column='idTahunAjaran', primary_key=True)
    tahunajaran = models.CharField(db_column='TahunAjaran', max_length=60, blank=True, null=True) # Unique handled by unique_together
    tglmulai = models.DateField(db_column='TglMulai', blank=True, null=True)
    tglselesai = models.DateField(db_column='TglSelesai', blank=True, null=True)
    isactive = models.BooleanField(db_column='isActive') # Changed to BooleanField
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', related_name='tahunajaran_dibuat_guru', blank=True, null=True) # Added, related_name
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'tahunajaran'
        unique_together = (('tahunajaran', 'lembaga', 'guru_pembuat'),) # Sesuaikan jika guru_pembuat tidak perlu di unique

    def __str__(self):
       return self.tahunajaran

#5
class Matapelajaran(models.Model):
    id = models.AutoField(primary_key=True) # Added explicit PK
    namamapel = models.CharField(db_column='NamaMapel', max_length=100) # Unique handled by unique_together
    kodemapel = models.CharField(db_column='KodeMapel', max_length=45) # Unique handled by unique_together
    grupmapel = models.CharField(db_column='GrupMapel', max_length=45, blank=True, null=True)
    kurikulum = models.CharField(max_length=60, blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', related_name='mapel_dibuat_guru', blank=True, null=True) # Added, related_name
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'matapelajaran'
        unique_together = (
            ('namamapel', 'lembaga', 'guru_pembuat'), # Sesuaikan jika guru_pembuat tidak perlu di unique
            ('kodemapel', 'lembaga', 'guru_pembuat'), # Sesuaikan jika guru_pembuat tidak perlu di unique
        )
    def __str__(self):
        return self.namamapel

#6
class Kelas(models.Model):
    idkelas = models.AutoField(primary_key=True)
    namakelas = models.CharField(db_column='NamaKelas', max_length=50, blank=True, null=True) # Unique handled by unique_together
    guru_walikelas = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru', blank=True, null=True, verbose_name="Wali Kelas") # Renamed for clarity
    tingkat = models.IntegerField(choices=TINGKAT_CHOICES, db_comment='7,8,9,10,11,12')
    jurusan = models.CharField(max_length=50, blank=True, null=True, choices=JURUSAN_CHOICES)
    tahunajaran = models.ForeignKey('Tahunajaran', on_delete=models.CASCADE, db_column='TahunAjaran_idTahunAjaran')
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', related_name='kelas_dibuat_guru', blank=True, null=True) # Added, added related_name
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'kelas'
        unique_together = (('namakelas', 'tahunajaran', 'lembaga', 'guru_pembuat'),) # Sesuaikan jika guru_pembuat tidak perlu di unique

    def __str__(self):
        wali_kelas_nama = self.guru_walikelas.nama_lengkap if self.guru_walikelas else "Belum ada wali kelas"
        return f"Kelas {self.namakelas} (Tingkat: {self.tingkat}, Wali Kelas: {wali_kelas_nama})"

#7
class Jeniskegiatanguru(models.Model):
    idjeniskegiatanguru = models.AutoField(db_column='idjenisKegiatanGuru', primary_key=True)
    namakegiatan = models.CharField(db_column='namaKegiatan', max_length=100) # Unique handled by unique_together
    iskbm = models.BooleanField(db_column='isKBM') # Changed to BooleanField
    volumejam = models.DecimalField(db_column='volumeJam', max_digits=4, decimal_places=2, blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'jeniskegiatanguru'
        unique_together = (('namakegiatan', 'lembaga', 'guru_pembuat'),) # Sesuaikan jika guru_pembuat tidak perlu di unique

#8
class Tugastambahan(models.Model):
    idtugastambahan = models.AutoField(db_column='idTugasTambahan', primary_key=True) # Added explicit PK
    namatugastambahan = models.CharField(db_column='NamaTugasTambahan', max_length=70) # Unique handled by unique_together
    inisialtugastambahan = models.CharField(db_column='InisialTugasTambahan', max_length=45, blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', related_name='tugas_tambahan_dibuat_guru', blank=True, null=True) # Added, related_name
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'tugastambahan'
        unique_together = (('namatugastambahan', 'lembaga', 'guru_pembuat'),) # Sesuaikan jika guru_pembuat tidak perlu di unique

#9
class Pesertadidik(models.Model):
    JENIS_SISWA_CHOICES = [
        ('Reguler', 'Reguler'),
        ('VIP/Khusus', 'VIP/Khusus'),
        ('Beasiswa Penuh', 'Beasiswa Penuh'),
        ('Beasiswa Temporer', 'Beasiswa Temporer'),
    ]
    STATUS_PD_CHOICES = [ # Added choices for status_pd
        ('Aktif', 'Aktif'),
        ('Lulus', 'Lulus'),
        ('Pindah', 'Pindah'),
        ('Drop Out', 'Drop Out'),
    ]

    idpesertadidik = models.AutoField(db_column='idpesertaDidik', primary_key=True)
    namalengkappd = models.CharField(db_column='namaLengkapPD', max_length=255)
    nis = models.CharField(db_column='NIS', max_length=20, blank=True, null=True) # Unique handled by unique_together
    nisn = models.CharField(db_column='NISN', max_length=20, blank=True, null=True) # Unique handled by unique_together
    gender = models.CharField(max_length=15)
    tgllahir = models.DateField(db_column='tglLahir', blank=True, null=True)
    jenis_siswa = models.CharField(max_length=50, choices=JENIS_SISWA_CHOICES, default='Reguler')
    is_berkebutuhan_khusus = models.BooleanField(default=False)
    status_pd = models.CharField(max_length=50, choices=STATUS_PD_CHOICES, default='Aktif', db_column='status_pd') # Added
    tgl_lulus = models.DateField(db_column='tgl_lulus', blank=True, null=True) # Added
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', related_name='siswa_dibuat_guru', blank=True, null=True) # Added, related_name
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'pesertadidik'
        unique_together = (
            ('nis', 'lembaga', 'guru_pembuat'), # Sesuaikan jika guru_pembuat tidak perlu di unique
            ('nisn', 'lembaga', 'guru_pembuat'), # Sesuaikan jika guru_pembuat tidak perlu di unique
        )

    def __str__(self):
        return self.namalengkappd

#10
class AlumniData(models.Model):
    idalumni = models.AutoField(primary_key=True)
    pesertadidik = models.OneToOneField(Pesertadidik, on_delete=models.CASCADE, db_column='pesertaDidik_idpesertaDidik') # OneToOneField karena UNIQUE INDEX di SQL
    tahun_lulus = models.SmallIntegerField() # YEAR di MySQL bisa jadi SmallIntegerField di Django
    kontak_email_alumni = models.CharField(max_length=255, blank=True, null=True)
    kontak_telepon_alumni = models.CharField(max_length=50, blank=True, null=True)
    pendidikan_lanjut = models.CharField(max_length=255, blank=True, null=True)
    pekerjaan_saat_ini = models.CharField(max_length=255, blank=True, null=True)
    catatan_alumni = models.TextField(blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'alumni_data'
        # unique_together = (('pesertaDidik', 'tahun_lulus'),) # Jika siswa bisa lulus beberapa kali di tahun yang berbeda?
        # Tidak perlu unique_together karena sudah OneToOneField ke pesertaDidik

#11
class JadwalPelajaran(models.Model):
    HARI_MINGGU_CHOICES = [
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
        ('Minggu', 'Minggu'),
    ]
    STATUS_JADWAL_CHOICES = [
        ('Aktif', 'Aktif'),
        ('Nonaktif', 'Nonaktif'),
        ('Dibatalkan', 'Dibatalkan'),
    ]

    idjadwal = models.AutoField(primary_key=True)
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, db_column='guru_idguru')
    matapelajaran = models.ForeignKey(Matapelajaran, on_delete=models.CASCADE, db_column='MataPelajaran_id')
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, db_column='kelas_idkelas')
    tahunajaran = models.ForeignKey(Tahunajaran, on_delete=models.CASCADE, db_column='TahunAjaran_idTahunAjaran')
    hari_minggu = models.CharField(max_length=10, choices=HARI_MINGGU_CHOICES)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    ruangan = models.CharField(max_length=100, blank=True, null=True)
    keterangan = models.CharField(max_length=255, blank=True, null=True)
    status_jadwal = models.CharField(max_length=50, choices=STATUS_JADWAL_CHOICES, default='Aktif')
    lembaga = models.ForeignKey(LembagaPendidikan, on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'jadwal_pelajaran'
        unique_together = (('guru', 'kelas', 'tahunajaran', 'hari_minggu', 'jam_mulai', 'lembaga'),)

    def __str__(self):
        return f"{self.matapelajaran.namamapel} - {self.kelas.namakelas} ({self.hari_minggu}, {self.jam_mulai}-{self.jam_selesai})"

#12
class Kegiatankbm(models.Model):
    idkegiatankbm = models.AutoField(db_column='idkegiatanKBM', primary_key=True)
    tglkbm = models.DateField(db_column='tglKBM')
    jamke = models.CharField(db_column='jamKe', max_length=45)
    materiajar = models.CharField(db_column='materiAjar', max_length=255)
    penugasan = models.CharField(max_length=255, blank=True, null=True)
    catatantambahan = models.CharField(db_column='catatanTambahan', max_length=255, blank=True, null=True)
    jumlahhadirpd = models.IntegerField(db_column='jumlahHadirPD') # Field ini akan disimpan langsung
    statuskbm = models.CharField(db_column='statusKBM', max_length=45, default='selesai')
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, db_column='guru_idguru')
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE, db_column='kelas_idkelas')
    matapelajaran = models.ForeignKey('Matapelajaran', on_delete=models.CASCADE, db_column='MataPelajaran_id')
    jadwal = models.ForeignKey('JadwalPelajaran', on_delete=models.SET_NULL, db_column='jadwal_idjadwal', blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'kegiatankbm'
        unique_together = (('guru', 'matapelajaran', 'kelas', 'tglkbm', 'jamke', 'lembaga'),)

#13
class Absensipd(models.Model):
    idabsensipd = models.AutoField(db_column='idabsensiPD', primary_key=True)
    pesertadidik = models.ForeignKey('Pesertadidik', on_delete=models.CASCADE, db_column='pesertaDidik_idpesertaDidik')
    kegiatankbm = models.ForeignKey('Kegiatankbm', on_delete=models.SET_NULL, db_column='kegiatanKBM_idkegiatanKBM', blank=True, null=True)
    statushadir = models.CharField(db_column='statusHadir', max_length=20, blank=True, null=True)
    catatan = models.CharField(max_length=50, blank=True, null=True)
    tglabsensi = models.DateField(db_column='tglAbsensi')
    jenisabsensi = models.CharField(db_column='jenisAbsensi', max_length=100, default='Absensi KBM')
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'absensipd'
        unique_together = (('pesertadidik', 'kegiatankbm'),) # mencegah duplikasi absensi per kbm

#14
class Catatankegiatanguru(models.Model):
    idcatatankegiatanguru = models.AutoField(db_column='idcatatanKegiatanGuru', primary_key=True)
    guru = models.ForeignKey('Guru', on_delete=models.CASCADE, db_column='guru_idguru')
    jeniskegiatanguru = models.ForeignKey('Jeniskegiatanguru', on_delete=models.CASCADE, db_column='jenisKegiatanGuru_idjenisKegiatanGuru')
    tglkegiatan = models.DateField(db_column='tglKegiatan')
    deskripsi = models.CharField(max_length=100)
    voljam = models.DecimalField(db_column='volJam', max_digits=4, decimal_places=2)
    outputkegiatan = models.CharField(db_column='outputKegiatan', max_length=100, blank=True, null=True)
    kegiatankbm = models.ForeignKey('Kegiatankbm', on_delete=models.SET_NULL, db_column='kegiatanKBM_idkegiatanKBM', blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Corrected
    updated_at = models.DateTimeField(auto_now=True, null=True) # Corrected

    class Meta:
        db_table = 'catatankegiatanguru'

#15
class Elemencapaian(models.Model):
    idelemencapaian = models.AutoField(db_column='idelemenCapaian', primary_key=True)
    tingkatkelas = models.IntegerField(db_column='tingkatKelas')
    kodecapaian = models.CharField(db_column='kodeCapaian', max_length=45) # Unique handled by unique_together
    deskripsielemen = models.CharField(db_column='deskripsiElemen', max_length=255)
    materiesensi = models.CharField(db_column='materiEsensi', max_length=255)
    matapelajaran = models.ForeignKey('Matapelajaran', on_delete=models.CASCADE, db_column='MataPelajaran_id')
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    guru_pembuat = models.ForeignKey('Guru', on_delete=models.SET_NULL, db_column='guru_idguru_pembuat', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        db_table = 'elemencapaian'
        unique_together = (('kodecapaian', 'lembaga'),) # Sesuaikan jika guru_pembuat tidak perlu di unique

#16
class Rpp(models.Model):
    STATUS_RPP_CHOICES = [ # Added choices for status_rpp
        ('Draft', 'Draft'),
        ('Siap', 'Siap'),
        ('Terverifikasi', 'Terverifikasi'),
    ]

    idrpp = models.AutoField(primary_key=True)
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, db_column='guru_idguru')
    matapelajaran = models.ForeignKey(Matapelajaran, on_delete=models.CASCADE, db_column='MataPelajaran_id')
    tahunajaran = models.ForeignKey('Tahunajaran', on_delete=models.CASCADE, db_column='TahunAjaran_idTahunAjaran')
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, db_column='kelas_idkelas')
    judulrpp = models.CharField(db_column='judulRPP', max_length=255)
    tglpembuatan = models.DateField(db_column='tglPembuatan')
    alokasiwaktu = models.DecimalField(db_column='alokasiWaktu', max_digits=4, decimal_places=2)
    tujuanpembelajaran = models.TextField(db_column='tujuanPembelajaran')
    materipembelajaran = models.TextField(db_column='materiPembelajaran')
    kegiatanpembuka = models.TextField(db_column='kegiatanPembuka')
    kegiataninti = models.TextField(db_column='kegiatanInti')
    kegiatanpenutup = models.TextField(db_column='kegiatanPenutup')
    penilaian = models.TextField()
    refleksi = models.TextField(blank=True, null=True)
    catatantambahan = models.TextField(db_column='catatanTambahan', blank=True, null=True)
    statusrpp = models.CharField(db_column='statusRPP', max_length=50, choices=STATUS_RPP_CHOICES, default='Draft') # Added choices and default
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Corrected
    updated_at = models.DateTimeField(auto_now=True, null=True) # Corrected

    class Meta:
        # managed = False # Hapus ini
        db_table = 'rpp'

#17
class ElemencapaianHasRpp(models.Model):
    elemencapaian = models.OneToOneField(Elemencapaian, on_delete=models.CASCADE, db_column='elemenCapaian_idelemenCapaian', primary_key=True)
    rpp = models.ForeignKey('Rpp', on_delete=models.CASCADE, db_column='rpp_idrpp')

    class Meta:
        db_table = 'elemencapaian_has_rpp'
        unique_together = (('elemencapaian', 'rpp'),) 

#18
class GuruHasMatapelajaran(models.Model):
    id = models.AutoField(primary_key=True) # Added
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, db_column='guru_idguru')
    matapelajaran = models.ForeignKey('Matapelajaran', on_delete=models.CASCADE, db_column='MataPelajaran_id')
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'guru_has_matapelajaran'
        unique_together = (('guru', 'matapelajaran', 'lembaga'),)

#19
class GuruHasTugastambahan(models.Model):
    id = models.AutoField(primary_key=True) # Added
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, db_column='guru_idguru')
    tugastambahan = models.ForeignKey('Tugastambahan', on_delete=models.CASCADE, db_column='TugasTambahan_idTugasTambahan')
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'guru_has_tugastambahan'
        unique_together = (('guru', 'tugastambahan', 'lembaga'),)

#20
class Masatugastambahan(models.Model):
    idmasatugastambahan = models.AutoField(db_column='idMasaTugasTambahan', primary_key=True)
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, db_column='guru_idguru')
    tugastambahan = models.ForeignKey('Tugastambahan', on_delete=models.CASCADE, db_column='TugasTambahan_idTugasTambahan')
    tahunajaran = models.ForeignKey('Tahunajaran', on_delete=models.CASCADE, db_column='TahunAjaran_idTahunAjaran')
    tglmulaitugas = models.DateField(db_column='tglMulaiTugas')
    tglselesaitugas = models.DateField(db_column='tglSelesaiTugas', blank=True, null=True)
    statustugas = models.CharField(db_column='statusTugas', max_length=50, blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'masatugastambahan'
        unique_together = (('guru', 'tugastambahan', 'tahunajaran', 'lembaga'),) # Added unique_together

#21
class Riwayatkelaspd(models.Model):
    idriwayatkelaspd = models.AutoField(db_column='idriwayatKelasPD', primary_key=True)
    pesertadidik = models.ForeignKey(Pesertadidik, on_delete=models.CASCADE, db_column='pesertaDidik_idpesertaDidik')
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, db_column='kelas_idkelas')
    tahunajaran = models.ForeignKey('Tahunajaran', on_delete=models.CASCADE, db_column='TahunAjaran_idTahunAjaran')
    tglmulai = models.DateField(db_column='tglMulai')
    tglselesai = models.DateField(db_column='tglSelesai', blank=True, null=True)
    ket = models.CharField(max_length=65, blank=True, null=True)
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'riwayatkelaspd'
        unique_together = (('pesertadidik', 'kelas', 'tahunajaran', 'lembaga'),) # Added

#22
class Sumberrpp(models.Model):
    idsumberrpp = models.AutoField(db_column='idsumberRPP', primary_key=True)
    rpp = models.ForeignKey(Rpp, on_delete=models.CASCADE, db_column='rpp_idrpp')
    jenissumber = models.CharField(db_column='jenisSumber', max_length=100)
    deskripsisumber = models.TextField(db_column='deskripsiSumber', blank=True, null=True)
    urlfile = models.CharField(db_column='urlFile', max_length=255, blank=True, null=True) # Consider FileField if files are uploaded
    lembaga = models.ForeignKey('LembagaPendidikan', on_delete=models.SET_NULL, db_column='lembaga_idlembaga', blank=True, null=True) # Added
    created_at = models.DateTimeField(auto_now_add=True) # Added
    updated_at = models.DateTimeField(auto_now=True, null=True) # Added

    class Meta:
        # managed = False # Hapus ini
        db_table = 'sumberrpp'


