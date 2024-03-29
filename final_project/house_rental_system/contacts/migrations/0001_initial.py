# Generated by Django 4.1.4 on 2023-01-19 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annonce', models.CharField(max_length=200)),
                ('annonce_id', models.IntegerField()),
                ('nom', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date_contact', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
