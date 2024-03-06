# Generated by Django 4.0.10 on 2024-03-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(max_length=15)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(max_length=15, upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
