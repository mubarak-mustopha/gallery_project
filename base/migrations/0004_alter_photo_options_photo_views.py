# Generated by Django 4.0.10 on 2024-03-09 09:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_photo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-created', '-id']},
        ),
        migrations.AddField(
            model_name='photo',
            name='views',
            field=models.ManyToManyField(related_name='photos_viewed', to=settings.AUTH_USER_MODEL),
        ),
    ]
