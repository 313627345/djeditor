# Generated by Django 3.2.13 on 2023-10-18 03:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='des',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name=''),
        ),
    ]
