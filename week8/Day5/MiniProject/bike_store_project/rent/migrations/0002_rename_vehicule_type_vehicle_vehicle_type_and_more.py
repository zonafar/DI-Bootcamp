# Generated by Django 4.1.3 on 2022-12-05 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicule_type',
            new_name='vehicle_type',
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date_created',
            field=models.DateField(verbose_name=datetime.datetime(2022, 12, 5, 11, 17, 9, 217679, tzinfo=datetime.timezone.utc)),
        ),
    ]
