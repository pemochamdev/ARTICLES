# Generated by Django 4.2.5 on 2023-09-30 19:59

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_alter_profile_picture_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture_profile',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=authy.models.user_directory_path),
        ),
    ]
