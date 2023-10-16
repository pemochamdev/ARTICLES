# Generated by Django 4.2.5 on 2023-09-27 20:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
    ]