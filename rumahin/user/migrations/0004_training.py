# Generated by Django 5.0.6 on 2024-06-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_modelregresi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.TextField(max_length=255)),
                ('harga', models.FloatField(max_length=100)),
                ('kecamatan', models.IntegerField()),
                ('link', models.TextField(max_length=20)),
                ('images_link', models.TextField(max_length=100)),
                ('kamar_tidur', models.FloatField(max_length=100)),
                ('kamar_mandi', models.FloatField(max_length=100)),
                ('luas_tanah', models.FloatField(max_length=100)),
                ('luas_bangunan', models.FloatField(max_length=100)),
                ('carport', models.FloatField(max_length=100)),
                ('sertifikat', models.IntegerField()),
                ('daya_listrik', models.FloatField(max_length=100)),
                ('kamar_pembantu', models.FloatField(max_length=100)),
                ('kamar_mandi_pembantu', models.FloatField(max_length=100)),
                ('dapur', models.FloatField(max_length=100)),
                ('ruang_makan', models.IntegerField()),
                ('ruang_tamu', models.IntegerField()),
                ('kondisi_perabotan', models.IntegerField()),
                ('jumlah_lantai', models.FloatField(max_length=100)),
                ('hadap', models.IntegerField()),
                ('konsep_dan_gaya_rumah', models.IntegerField()),
                ('pemandangan', models.IntegerField()),
                ('terjangkau_internet', models.IntegerField()),
                ('lebar_jalan', models.FloatField(max_length=100)),
                ('tahun_dibangun', models.FloatField(max_length=100)),
                ('tahun_di_renovasi', models.FloatField(max_length=100)),
                ('sumber_air', models.IntegerField()),
                ('hook', models.IntegerField()),
                ('kondisi_properti', models.IntegerField()),
                ('garasi', models.IntegerField()),
                ('distance_gerbangtol', models.FloatField(max_length=100)),
                ('distance_school', models.FloatField(max_length=100)),
                ('distance_hospital', models.FloatField(max_length=100)),
                ('distance_tokoobat', models.FloatField(max_length=100)),
                ('bata_hebel', models.IntegerField(default=0)),
                ('bata_merah', models.IntegerField(default=0)),
                ('batako', models.IntegerField(default=0)),
                ('beton', models.IntegerField(default=0)),
                ('granit', models.IntegerField(default=0)),
                ('keramik', models.IntegerField(default=0)),
                ('marmer', models.IntegerField(default=0)),
                ('ubin', models.IntegerField(default=0)),
                ('vinyl', models.IntegerField(default=0)),
                ('ac', models.IntegerField(default=0)),
                ('akses_parkir', models.IntegerField(default=0)),
                ('balcony', models.IntegerField(default=0)),
                ('built_in_robes', models.IntegerField(default=0)),
                ('cctv', models.IntegerField(default=0)),
                ('golf_view', models.IntegerField(default=0)),
                ('jalur_telepon', models.IntegerField(default=0)),
                ('jogging_track', models.IntegerField(default=0)),
                ('keamanan', models.IntegerField(default=0)),
                ('kitchen_set', models.IntegerField(default=0)),
                ('kolam_ikan', models.IntegerField(default=0)),
                ('kolam_renang', models.IntegerField(default=0)),
                ('lapangan_basket', models.IntegerField(default=0)),
                ('lapangan_bola', models.IntegerField(default=0)),
                ('lapangan_bulu_tangkis', models.IntegerField(default=0)),
                ('lapangan_tenis', models.IntegerField(default=0)),
                ('lapangan_voli', models.IntegerField(default=0)),
                ('masjid', models.IntegerField(default=0)),
                ('one_gate_system', models.IntegerField(default=0)),
                ('pemanas_air', models.IntegerField(default=0)),
                ('separate_dining_room', models.IntegerField(default=0)),
                ('taman', models.IntegerField(default=0)),
                ('tempat_gym', models.IntegerField(default=0)),
                ('tempat_jemuran', models.IntegerField(default=0)),
                ('tempat_laundry', models.IntegerField(default=0)),
                ('wastafel', models.IntegerField(default=0)),
                ('kecamatan_1', models.CharField(max_length=255)),
                ('latitude', models.FloatField(max_length=100)),
                ('longitude', models.FloatField(max_length=100)),
                ('label', models.IntegerField()),
            ],
        ),
    ]
