# Generated by Django 4.1.2 on 2022-10-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_animal_image_alter_animal_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
