# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from PIL import Image # <--- Import Pillow

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


class Absensipd(models.Model):
    idabsensipd = models.AutoField(db_column='idabsensiPD', primary_key=True)  # Field name made lowercase.
    statushadir = models.CharField(db_column='statusHadir', max_length=20, blank=True, null=True, db_comment="Hadir', 'Izin', 'Sakit', 'Alpha")  # Field name made lowercase.
    catatan = models.CharField(max_length=50, blank=True, null=True)
    kegiatankbm_idkegiatankbm = models.ForeignKey('Kegiatankbm', models.DO_NOTHING, db_column='kegiatanKBM_idkegiatanKBM', blank=True, null=True)  # Field name made lowercase.
    pesertadidik_idpesertadidik = models.ForeignKey('Pesertadidik', models.DO_NOTHING, db_column='pesertaDidik_idpesertaDidik')  # Field name made lowercase.
    tglabsensi = models.DateField(db_column='tglAbsensi')  # Field name made lowercase.
    jenisabsensi = models.CharField(db_column='jenisAbsensi', max_length=100, db_comment='berupa Absensi KBM, Absensi Upacara, Absensi dhuha, dll')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'absensipd'


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


class Catatankegiatanguru(models.Model):
    idcatatankegiatanguru = models.AutoField(db_column='idcatatanKegiatanGuru', primary_key=True)  # Field name made lowercase.
    tglkegiatan = models.DateField(db_column='tglKegiatan')  # Field name made lowercase.
    deskripsi = models.CharField(max_length=100)
    voljam = models.DecimalField(db_column='volJam', max_digits=4, decimal_places=2)  # Field name made lowercase.
    outputkegiatan = models.CharField(db_column='outputKegiatan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    guru_idguru = models.ForeignKey('Guru', models.DO_NOTHING, db_column='guru_idguru')
    tahunajaran_idtahunajaran = models.ForeignKey('Tahunajaran', models.DO_NOTHING, db_column='TahunAjaran_idTahunAjaran')  # Field name made lowercase.
    jeniskegiatanguru_idjeniskegiatanguru = models.ForeignKey('Jeniskegiatanguru', models.DO_NOTHING, db_column='jenisKegiatanGuru_idjenisKegiatanGuru')  # Field name made lowercase.
    kegiatankbm_idkegiatankbm = models.ForeignKey('Kegiatankbm', models.DO_NOTHING, db_column='kegiatanKBM_idkegiatanKBM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catatankegiatanguru'


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


class Elemencapaian(models.Model):
    idelemencapaian = models.AutoField(db_column='idelemenCapaian', primary_key=True)  # Field name made lowercase.
    tingkatkelas = models.IntegerField(db_column='tingkatKelas')  # Field name made lowercase.
    kodecapaian = models.CharField(db_column='kodeCapaian', unique=True, max_length=45, db_comment='kode tujuan kompetensi, sebaiknya dibuatkan saja manual daftar kode tujuan ')  # Field name made lowercase.
    deskripsielemen = models.CharField(db_column='deskripsiElemen', max_length=255, db_comment='deskripsi tujuan kompetensi')  # Field name made lowercase.
    materiesensi = models.CharField(db_column='materiEsensi', max_length=255, db_comment='list materi pokok yang wajib diajarkan untuk memenuhi standar minimal capaian')  # Field name made lowercase.
    matapelajaran = models.ForeignKey('Matapelajaran', models.DO_NOTHING, db_column='MataPelajaran_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemencapaian'

#GANTI KRN ERROR
class ElemencapaianHasRpp(models.Model):
    elemencapaian_idelemencapaian = models.ForeignKey(Elemencapaian, models.DO_NOTHING, db_column='elemenCapaian_idelemenCapaian')
    rpp_idrpp = models.ForeignKey('Rpp', models.DO_NOTHING, db_column='rpp_idrpp')

    class Meta:
        managed = False
        db_table = 'elemencapaian_has_rpp'


class Guru(models.Model):
    idguru = models.AutoField(primary_key=True)
    nama_lengkap = models.CharField(max_length=255)
    nip = models.CharField(max_length=20, blank=True, null=True)
    nuptk = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=150)
    pwd = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='guru_photos/', blank=True, null=True)
    nama_instansi = models.CharField(max_length=255, default='')
    alamat = models.TextField(blank=True, null=True) # TextField cocok untuk alamat yang panjang
    
    class Meta:
        managed = False
        db_table = 'guru'
    
    # TAMBAHKAN ATAU PASTIKAN METODE __str__ INI ADA
    def __str__(self):
        return self.nama_lengkap # Akan menampilkan Nama Lengkap Guru di dropdown
    
     # --- TAMBAHKAN METODE SAVE KUSTOM INI utk upload foto ---
    def save(self, *args, **kwargs):
        # Pertama, jalankan proses save standar
        super().save(*args, **kwargs)

        # Jika ada file foto yang diunggah
        if self.foto:
            img = Image.open(self.foto.path)

            # Tentukan ukuran maksimum (misal: 800x800 pixels)
            output_size = (800, 800)

            # Ubah ukuran gambar jika lebih besar dari ukuran maksimum
            if img.height > output_size[0] or img.width > output_size[1]:
                img.thumbnail(output_size)
                img.save(self.foto.path, quality=85, optimize=True) # Simpan kembali dengan kualitas 85%


class GuruHasMatapelajaran(models.Model):
    guru_idguru = models.ForeignKey(Guru, models.DO_NOTHING, db_column='guru_idguru')
    matapelajaran = models.ForeignKey('Matapelajaran', models.DO_NOTHING, db_column='MataPelajaran_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guru_has_matapelajaran'


class GuruHasTugastambahan(models.Model):
    guru_idguru = models.ForeignKey(Guru, models.DO_NOTHING, db_column='guru_idguru')
    tugastambahan_idtugastambahan = models.ForeignKey('Tugastambahan', models.DO_NOTHING, db_column='TugasTambahan_idTugasTambahan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guru_has_tugastambahan'


class Jeniskegiatanguru(models.Model):
    idjeniskegiatanguru = models.AutoField(db_column='idjenisKegiatanGuru', primary_key=True)  # Field name made lowercase.
    namakegiatan = models.CharField(db_column='namaKegiatan', max_length=100)  # Field name made lowercase.
    iskbm = models.IntegerField(db_column='isKBM')  # Field name made lowercase.
    volumejam = models.DecimalField(db_column='volumeJam', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jeniskegiatanguru'


class Kegiatankbm(models.Model):
    idkegiatankbm = models.AutoField(db_column='idkegiatanKBM', primary_key=True)  # Field name made lowercase.
    tglkbm = models.DateField(db_column='tglKBM')  # Field name made lowercase.
    jamke = models.CharField(db_column='jamKe', max_length=45, db_comment='isian dapat berupa: 1 atau 3 atau 1-3 ')  # Field name made lowercase.
    materiajar = models.CharField(db_column='materiAjar', max_length=255)  # Field name made lowercase.
    penugasan = models.CharField(max_length=255, blank=True, null=True)
    catatantambahan = models.CharField(db_column='catatanTambahan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jumlahhadirpd = models.IntegerField(db_column='jumlahHadirPD')  # Field name made lowercase.
    statuskbm = models.CharField(db_column='statusKBM', max_length=45, db_comment='selesai, belum selesai, dibatalkan')  # Field name made lowercase.
    tahunajaran_idtahunajaran = models.ForeignKey('Tahunajaran', models.DO_NOTHING, db_column='TahunAjaran_idTahunAjaran')  # Field name made lowercase.
    kelas_idkelas = models.ForeignKey('Kelas', models.DO_NOTHING, db_column='kelas_idkelas')
    matapelajaran = models.ForeignKey('Matapelajaran', models.DO_NOTHING, db_column='MataPelajaran_id')  # Field name made lowercase.
    guru_idguru = models.ForeignKey(Guru, models.DO_NOTHING, db_column='guru_idguru')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kegiatankbm'
        unique_together = (('guru_idguru', 'matapelajaran', 'kelas_idkelas', 'tglkbm', 'jamke'),)


class Kelas(models.Model):
    idkelas = models.AutoField(primary_key=True)
    namakelas = models.CharField(db_column='NamaKelas', max_length=50, blank=True, null=True)
    guru_idguru = models.ForeignKey('Guru', models.DO_NOTHING, db_column='guru_idguru', blank=True, null=True)
    tingkat = models.IntegerField(db_comment='7,8,9,10,11,12', choices=TINGKAT_CHOICES)
    jurusan = models.CharField(max_length=50, blank=True, null=True, db_comment='UMUM, IPA, IPS, BAHASA', choices=JURUSAN_CHOICES)
    tahunajaran_idtahunajaran = models.ForeignKey('Tahunajaran', models.DO_NOTHING, db_column='TahunAjaran_idTahunAjaran')

    class Meta:
        managed = False
        db_table = 'kelas'

    # UBAH ATAU TAMBAHKAN METODE __str__ INI
    def __str__(self):
        # Mengakses nama guru melalui FK. Jika guru_idguru null, tampilkan 'Belum ada wali kelas'.
        wali_kelas_nama = self.guru_idguru.nama_lengkap if self.guru_idguru else "Belum ada wali kelas"
        return f"Kelas {self.namakelas} (Tingkat: {self.tingkat}, Wali Kelas: {wali_kelas_nama})"


class Masatugastambahan(models.Model):
    idmasatugastambahan = models.AutoField(db_column='idMasaTugasTambahan', primary_key=True)  # Field name made lowercase.
    tglmulaitugas = models.DateField(db_column='tglMulaiTugas')  # Field name made lowercase.
    tglselesaitugas = models.DateField(db_column='tglSelesaiTugas', blank=True, null=True)  # Field name made lowercase.
    statustugas = models.CharField(db_column='statusTugas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guru_idguru = models.ForeignKey(Guru, models.DO_NOTHING, db_column='guru_idguru')
    tugastambahan_idtugastambahan = models.ForeignKey('Tugastambahan', models.DO_NOTHING, db_column='TugasTambahan_idTugasTambahan')  # Field name made lowercase.
    tahunajaran_idtahunajaran = models.ForeignKey('Tahunajaran', models.DO_NOTHING, db_column='TahunAjaran_idTahunAjaran')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masatugastambahan'


class Matapelajaran(models.Model):
    namamapel = models.CharField(db_column='NamaMapel', unique=True, max_length=100)  # Field name made lowercase.
    kodemapel = models.CharField(db_column='KodeMapel', unique=True, max_length=45)  # Field name made lowercase.
    grupmapel = models.CharField(db_column='GrupMapel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    kurikulum = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matapelajaran'


class Pesertadidik(models.Model):
    idpesertadidik = models.AutoField(db_column='idpesertaDidik', primary_key=True)  # Field name made lowercase.
    namalengkappd = models.CharField(db_column='namaLengkapPD', max_length=255)  # Field name made lowercase.
    nis = models.CharField(db_column='NIS', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    nisn = models.CharField(db_column='NISN', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=15)
    tgllahir = models.DateField(db_column='tglLahir', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pesertadidik'


class Riwayatkelaspd(models.Model):
    idriwayatkelaspd = models.AutoField(db_column='idriwayatKelasPD', primary_key=True)  # Field name made lowercase.
    tglmulai = models.DateField(db_column='tglMulai')  # Field name made lowercase.
    tglselesai = models.DateField(db_column='tglSelesai', blank=True, null=True)  # Field name made lowercase.
    ket = models.CharField(max_length=65, blank=True, null=True, db_comment='Alasan pindah kelas (misalnya, "Kenaikan Kelas", "Pindah Kelas")')
    pesertadidik_idpesertadidik = models.ForeignKey(Pesertadidik, models.DO_NOTHING, db_column='pesertaDidik_idpesertaDidik')  # Field name made lowercase.
    kelas_idkelas = models.ForeignKey(Kelas, models.DO_NOTHING, db_column='kelas_idkelas')
    tahunajaran_idtahunajaran = models.ForeignKey('Tahunajaran', models.DO_NOTHING, db_column='TahunAjaran_idTahunAjaran')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'riwayatkelaspd'


class Rpp(models.Model):
    idrpp = models.AutoField(primary_key=True)
    kurikulum = models.CharField(max_length=50, blank=True, null=True, db_comment='untuk ref cepat')
    guru_idguru = models.ForeignKey(Guru, models.DO_NOTHING, db_column='guru_idguru')
    tahunajaran_idtahunajaran = models.ForeignKey('Tahunajaran', models.DO_NOTHING, db_column='TahunAjaran_idTahunAjaran')  # Field name made lowercase.
    kelas_idkelas = models.ForeignKey(Kelas, models.DO_NOTHING, db_column='kelas_idkelas')
    matapelajaran = models.ForeignKey(Matapelajaran, models.DO_NOTHING, db_column='MataPelajaran_id')  # Field name made lowercase.
    judulrpp = models.CharField(db_column='judulRPP', max_length=255)  # Field name made lowercase.
    tglpembuatan = models.DateField(db_column='tglPembuatan')  # Field name made lowercase.
    alokasiwaktu = models.DecimalField(db_column='alokasiWaktu', max_digits=4, decimal_places=2)  # Field name made lowercase.
    tujuanpembelajaran = models.TextField(db_column='tujuanPembelajaran')  # Field name made lowercase.
    materipembelajaran = models.TextField(db_column='materiPembelajaran')  # Field name made lowercase.
    kegiatanpembuka = models.TextField(db_column='kegiatanPembuka')  # Field name made lowercase.
    kegiataninti = models.TextField(db_column='kegiatanInti')  # Field name made lowercase.
    kegiatanpenutup = models.TextField(db_column='kegiatanPenutup')  # Field name made lowercase.
    penilaian = models.TextField()
    refleksi = models.TextField(blank=True, null=True)
    catatantambahan = models.TextField(db_column='catatanTambahan', blank=True, null=True)  # Field name made lowercase.
    statusrpp = models.CharField(db_column='statusRPP', max_length=50, db_comment='draft, siap, terverifikasi')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rpp'


class Sumberrpp(models.Model):
    idsumberrpp = models.AutoField(db_column='idsumberRPP', primary_key=True)  # Field name made lowercase.
    jenissumber = models.CharField(db_column='jenisSumber', max_length=100)  # Field name made lowercase.
    deskripsisumber = models.TextField(db_column='deskripsiSumber', blank=True, null=True)  # Field name made lowercase.
    urlfile = models.CharField(db_column='urlFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rpp_idrpp = models.ForeignKey(Rpp, models.DO_NOTHING, db_column='rpp_idrpp')

    class Meta:
        managed = False
        db_table = 'sumberrpp'


class Tahunajaran(models.Model):
    idtahunajaran = models.AutoField(db_column='idTahunAjaran', primary_key=True)  # Field name made lowercase.
    tahunajaran = models.CharField(db_column='TahunAjaran', unique=True, max_length=60, blank=True, null=True)  # Field name made lowercase.
    tglmulai = models.DateField(db_column='TglMulai', blank=True, null=True)  # Field name made lowercase.
    tglselesai = models.DateField(db_column='TglSelesai', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tahunajaran'
    
    # TAMBAHKAN ATAU PASTIKAN METODE __str__ INI ADA
    def __str__(self):
       return self.tahunajaran 
       # return f"{self.tahun_mulai}/{self.tahun_selesai} - {self.semester}" # Akan menampilkan "2024/2025 - Ganjil"

class Tugastambahan(models.Model):
    idtugastambahan = models.AutoField(db_column='idTugasTambahan', primary_key=True)  # Field name made lowercase.
    namatugastambahan = models.CharField(db_column='NamaTugasTambahan', max_length=70)  # Field name made lowercase.
    inisialtugastambahan = models.CharField(db_column='InisialTugasTambahan', max_length=45, blank=True, null=True, db_comment='misal inisial Kurikulum adalah PKM KUR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tugastambahan'