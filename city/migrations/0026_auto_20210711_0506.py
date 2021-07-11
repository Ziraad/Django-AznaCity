# Generated by Django 3.0.8 on 2021-07-11 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0025_auto_20210711_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='great',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='great_views', to='city.IpClass', verbose_name='نمایش'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='hotel_views', to='city.IpClass', verbose_name='نمایش'),
        ),
        migrations.AddField(
            model_name='martyrs',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='martyrs_views', to='city.IpClass', verbose_name='نمایش'),
        ),
        migrations.AddField(
            model_name='place',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='place_views', to='city.IpClass', verbose_name='نمایش'),
        ),
        migrations.AddField(
            model_name='soghat',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='soghat_views', to='city.IpClass', verbose_name='نمایش'),
        ),
    ]