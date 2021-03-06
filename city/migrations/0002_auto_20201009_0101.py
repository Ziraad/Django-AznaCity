# Generated by Django 3.0.8 on 2020-10-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'شهر', 'verbose_name_plural': 'شهر'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'مکان', 'verbose_name_plural': 'مکان'},
        ),
        migrations.AlterModelOptions(
            name='soghat',
            options={'verbose_name': 'سوغات', 'verbose_name_plural': 'سوغات'},
        ),
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=40, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=40, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AddField(
            model_name='soghat',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=40, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(blank=True, choices=[('H', 'تاریخی'), ('M', 'مذهبی'), ('T', 'گردشگری'), ('R', 'روستا'), ('K', 'کارخانجات')], max_length=1, null=True, verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='soghat',
            name='category',
            field=models.CharField(blank=True, choices=[('F', 'خوراکی'), ('D', 'صنایع دستی')], max_length=1, null=True, verbose_name='دسته بندی'),
        ),
    ]
