# Generated by Django 3.0.8 on 2021-04-09 12:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0013_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
