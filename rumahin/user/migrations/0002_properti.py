# Generated by Django 5.0.6 on 2024-06-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=255, null=True)),
                ('harga', models.CharField(blank=True, max_length=100, null=True)),
                ('cicilan', models.CharField(blank=True, max_length=100, null=True)),
                ('kecamatan', models.CharField(blank=True, max_length=255, null=True)),
                ('luas_tanah_front', models.CharField(blank=True, max_length=100, null=True)),
                ('luas_bangunan_front', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('fasilitas', models.TextField(blank=True, null=True)),
                ('last_update', models.CharField(blank=True, max_length=100, null=True)),
                ('kamar_tidur', models.FloatField(blank=True, null=True)),
                ('kamar_mandi', models.FloatField(blank=True, null=True)),
                ('luas_tanah', models.CharField(blank=True, max_length=100, null=True)),
                ('luas_bangunan', models.CharField(blank=True, max_length=100, null=True)),
                ('carport', models.FloatField(blank=True, null=True)),
                ('tipe_properti', models.CharField(blank=True, max_length=255, null=True)),
                ('sertifikat', models.CharField(blank=True, max_length=100, null=True)),
                ('kamar_pembantu', models.FloatField(blank=True, null=True)),
                ('kamar_mandi_pembantu', models.FloatField(blank=True, null=True)),
                ('dapur', models.FloatField(blank=True, null=True)),
                ('ruang_makan', models.CharField(blank=True, max_length=255, null=True)),
                ('ruang_tamu', models.CharField(blank=True, max_length=255, null=True)),
                ('kondisi_perabotan', models.CharField(blank=True, max_length=255, null=True)),
                ('material_bangunan', models.CharField(blank=True, max_length=255, null=True)),
                ('material_lantai', models.CharField(blank=True, max_length=255, null=True)),
                ('jumlah_lantai', models.FloatField(blank=True, null=True)),
                ('hadap', models.CharField(blank=True, max_length=100, null=True)),
                ('konsep_dan_gaya_rumah', models.CharField(blank=True, max_length=255, null=True)),
                ('pemandangan', models.CharField(blank=True, max_length=255, null=True)),
                ('terjangkau_internet', models.CharField(blank=True, max_length=255, null=True)),
                ('lebar_jalan', models.CharField(blank=True, max_length=100, null=True)),
                ('tahun_dibangun', models.FloatField(blank=True, null=True)),
                ('tahun_di_renovasi', models.FloatField(blank=True, null=True)),
                ('sumber_air', models.CharField(blank=True, max_length=100, null=True)),
                ('hook', models.CharField(blank=True, max_length=100, null=True)),
                ('kondisi_properti', models.CharField(blank=True, max_length=255, null=True)),
                ('tipe_iklan', models.CharField(blank=True, max_length=100, null=True)),
                ('id_iklan', models.CharField(blank=True, max_length=100, null=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('daya_listrik', models.CharField(blank=True, max_length=100, null=True)),
                ('garasi', models.FloatField(blank=True, null=True)),
                ('nomor_lantai', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
