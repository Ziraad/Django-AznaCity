# Generated by Django 3.0.8 on 2021-07-15 10:49

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('city', '0026_auto_20210711_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='نام')),
                ('slug', models.SlugField(allow_unicode=True, help_text='نام دسته بندی را به انگلیسی ترجمه کنید و در این قسمت تایپ کنید!خط فاصله ها را با "-" پرکنید!', max_length=100, verbose_name='اسلاگ')),
                ('image', models.ImageField(blank=True, upload_to='CategoryImages/', verbose_name='تصویر')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='news.Category', verbose_name='سردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, help_text='عنوان را به انگلیسی ترجمه کنید و در این قسمت تایپ کنید!خط فاصله ها را با "-" پرکنید!', max_length=200, verbose_name='اسلاگ')),
                ('image', models.ImageField(blank=True, upload_to='newsImages/', verbose_name='تصویر')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='متن خبر')),
                ('study_time', models.IntegerField(verbose_name='زمان مطالعه')),
                ('selected_editor', models.BooleanField(default=False, null=True, verbose_name='منتخب سردبیر')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ انتشار')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile', verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='دسته بندی')),
                ('views', models.ManyToManyField(blank=True, related_name='post_views', to='city.IpClass', verbose_name='نمایش')),
            ],
            options={
                'verbose_name': 'اخبار',
                'verbose_name_plural': 'اخبار',
            },
        ),
    ]
