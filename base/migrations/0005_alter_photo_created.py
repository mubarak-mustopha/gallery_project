# Generated by Django 4.0.10 on 2024-07-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_photo_options_photo_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
