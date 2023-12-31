# Generated by Django 4.2.6 on 2023-11-01 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('logo', models.FileField(upload_to='')),
                ('president', models.CharField(blank=True, max_length=30)),
                ('coach', models.CharField(blank=True, max_length=30)),
                ('yili', models.DateField(blank=True)),
                ('record_transfer', models.CharField(blank=True, max_length=30)),
                ('record_sotuv', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Davlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tugulgan_sana', models.DateField()),
                ('narx', models.PositiveSmallIntegerField()),
                ('pozitsiya', models.CharField(max_length=30)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.club')),
                ('davlat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.davlat')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.PositiveSmallIntegerField()),
                ('tah_narx', models.PositiveSmallIntegerField()),
                ('mavsum', models.CharField(max_length=10)),
                ('eski_club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sotuvlari', to='asosiy.club')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.player')),
                ('yangi_club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olganlari', to='asosiy.club')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='davlat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.davlat'),
        ),
    ]
