# Generated by Django 4.0.10 on 2024-02-29 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_account', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
