# Generated by Django 5.0.6 on 2024-06-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_properti'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelRegresi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateField()),
                ('versi', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=500)),
            ],
        ),
    ]