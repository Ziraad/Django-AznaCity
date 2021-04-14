# Generated by Django 3.0.8 on 2020-08-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام شهر')),
                ('about', models.TextField(verbose_name='درباره شهر')),
                ('image', models.ImageField(upload_to='city', verbose_name='عکس')),
                ('dialect', models.CharField(max_length=20, verbose_name='گویش')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50, verbose_name='نام مکان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='place', verbose_name='عکس')),
                ('category', models.CharField(choices=[('H', 'تاریخی'), ('M', 'مذهبی'), ('T', 'گردشگری'), ('R', 'روستا'), ('K', 'کارخانجات')], max_length=1, verbose_name='دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='Soghat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام سوغات')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='soghat', verbose_name='عکس')),
                ('category', models.CharField(choices=[('F', 'خوراکی'), ('D', 'صنایع دستی')], max_length=1, verbose_name='دسته بندی')),
            ],
        ),
    ]