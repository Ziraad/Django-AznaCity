# Generated by Django 3.0.8 on 2020-10-08 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0003_auto_20201009_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place_name',
            new_name='name',
        ),
    ]
