# Generated by Django 3.0.8 on 2021-07-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0016_auto_20210413_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='categorys/icon', verbose_name='آیکون'),
        ),
    ]
