# Generated by Django 2.0.4 on 2018-05-06 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siklinik', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kelompok_pasien',
            name='registrasi',
        ),
        migrations.AddField(
            model_name='registrasi',
            name='kelpasien',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='siklinik.Kelompok_Pasien'),
        ),
    ]