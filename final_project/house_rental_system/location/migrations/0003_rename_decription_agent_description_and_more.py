# Generated by Django 4.1.4 on 2023-01-12 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_remove_agent_phone_alter_agent_date_embauche_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='decription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='decription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='is_publised',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='agent',
            name='date_embauche',
            field=models.DateField(default=datetime.datetime(2023, 1, 12, 11, 11, 43, 783584, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='date_annonce',
            field=models.DateField(default=datetime.datetime(2023, 1, 12, 11, 11, 43, 783584, tzinfo=datetime.timezone.utc)),
        ),
    ]
