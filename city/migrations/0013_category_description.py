# Generated by Django 3.0.8 on 2021-04-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0012_hotel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
