# Generated by Django 4.1.2 on 2022-10-24 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_alter_animal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='image',
        ),
    ]
