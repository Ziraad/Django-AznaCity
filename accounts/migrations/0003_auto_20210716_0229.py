# Generated by Django 3.0.8 on 2021-07-15 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210715_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='تلفن همراه'),
        ),
    ]
