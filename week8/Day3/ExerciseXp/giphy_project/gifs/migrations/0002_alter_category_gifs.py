# Generated by Django 4.1.2 on 2022-11-03 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gifs',
            field=models.ManyToManyField(blank=True, related_name='categories', to='gifs.gif'),
        ),
    ]
