# Generated by Django 3.0.8 on 2021-01-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0010_martyrs_will'),
    ]

    operations = [
        migrations.AlterField(
            model_name='great',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='great',
            name='date_of_death',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='تاریخ وفات'),
        ),
        migrations.AlterField(
            model_name='martyrs',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='martyrs',
            name='date_of_death',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='تاریخ شهادت'),
        ),
        migrations.AlterField(
            model_name='martyrs',
            name='operation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عملیات'),
        ),
    ]