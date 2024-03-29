# Generated by Django 4.1.4 on 2023-01-11 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=60)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('decription', models.TextField()),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('is_MVP', models.BooleanField(default=False)),
                ('date_embauche', models.DateField(default=datetime.datetime(2023, 1, 11, 20, 11, 43, 834271, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=200)),
                ('adresse', models.CharField(blank=True, max_length=125)),
                ('decription', models.TextField(verbose_name='description')),
                ('ville', models.CharField(blank=True, max_length=100)),
                ('secteur', models.CharField(blank=True, max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('code_postal', models.CharField(blank=True, max_length=20)),
                ('prix', models.IntegerField()),
                ('chambres', models.SmallIntegerField(default=0)),
                ('douches', models.SmallIntegerField(default=0)),
                ('garages', models.SmallIntegerField(default=0)),
                ('taille', models.DecimalField(decimal_places=1, max_digits=6)),
                ('date_annonce', models.DateField(default=datetime.datetime(2023, 1, 11, 20, 11, 43, 834271, tzinfo=datetime.timezone.utc))),
                ('is_publised', models.BooleanField(default=True)),
                ('photo_majeure', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('agent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.agent')),
            ],
        ),
    ]
