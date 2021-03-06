# Generated by Django 2.0.4 on 2018-05-03 12:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Alat_Kesehatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('harga_dasar', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Farmasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('tanggal', models.DateField()),
                ('no_transaksi', models.CharField(max_length=90)),
                ('diskon', models.DecimalField(decimal_places=2, max_digits=3)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Farmasi_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.IntegerField()),
                ('diskon', models.DecimalField(decimal_places=2, max_digits=3)),
                ('total', models.DecimalField(decimal_places=2, max_digits=3)),
                ('farmasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Farmasi')),
            ],
        ),
        migrations.CreateModel(
            name='Harga_Jual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=15)),
                ('harga_beli', models.DecimalField(decimal_places=2, max_digits=15)),
                ('alkes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Alat_Kesehatan')),
            ],
        ),
        migrations.CreateModel(
            name='Jenis_Kelamin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Kasir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kwitansi', models.CharField(max_length=90)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori_Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori_Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Kelompok_Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('margin', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('harga_dasar', models.DecimalField(decimal_places=2, max_digits=15)),
                ('harga_beli', models.DecimalField(decimal_places=2, max_digits=15)),
                ('kb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Kategori_Barang')),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('tempat_lahir', models.CharField(max_length=25)),
                ('tangal_lahir', models.DateField()),
                ('alamat', models.TextField()),
                ('rt', models.CharField(max_length=5)),
                ('rw', models.CharField(max_length=5)),
                ('kodepos', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telepon', models.CharField(max_length=25)),
                ('status_kawin', models.CharField(max_length=12)),
                ('agama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Agama')),
                ('jk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Jenis_Kelamin')),
            ],
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('tempat_lahir', models.CharField(max_length=25)),
                ('tangal_lahir', models.DateField()),
                ('alamat', models.TextField()),
                ('rt', models.CharField(max_length=5)),
                ('rw', models.CharField(max_length=5)),
                ('kodepos', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telepon', models.CharField(max_length=25)),
                ('status_kawin', models.CharField(max_length=12)),
                ('agama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Agama')),
                ('jk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Jenis_Kelamin')),
                ('kp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Kategori_Pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='Pekerjaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Registrasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('no_register', models.CharField(max_length=90)),
                ('no_antrian', models.IntegerField()),
                ('pasien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Pasien')),
                ('pegawai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='Rekam_Medis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosa', models.CharField(max_length=90)),
                ('keterangan_diagnosa', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('no_resep', models.CharField(max_length=90)),
                ('registrasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Registrasi')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tindakan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('harga', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('jenis_tindakan', models.IntegerField()),
                ('status', models.IntegerField()),
                ('alkes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Alat_Kesehatan')),
                ('obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Obat')),
                ('registrasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Registrasi')),
                ('tindakan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Tindakan')),
            ],
        ),
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=90)),
                ('kodepos', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='pegawai',
            name='wilayah',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Wilayah'),
        ),
        migrations.AddField(
            model_name='pasien',
            name='pekerjaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Pekerjaan'),
        ),
        migrations.AddField(
            model_name='pasien',
            name='wilayah',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Wilayah'),
        ),
        migrations.AddField(
            model_name='kelompok_pasien',
            name='registrasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Registrasi'),
        ),
        migrations.AddField(
            model_name='kasir',
            name='registrasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Registrasi'),
        ),
        migrations.AddField(
            model_name='harga_jual',
            name='kelpas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Kelompok_Pasien'),
        ),
        migrations.AddField(
            model_name='harga_jual',
            name='obat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Obat'),
        ),
        migrations.AddField(
            model_name='farmasi',
            name='registrasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Registrasi'),
        ),
        migrations.AddField(
            model_name='alat_kesehatan',
            name='kb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siklinik.Obat'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='pegawai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siklinik.Pegawai'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siklinik.Role'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
