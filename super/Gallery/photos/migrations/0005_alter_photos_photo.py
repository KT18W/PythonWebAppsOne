# Generated by Django 4.1 on 2022-10-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(upload_to='Photos/static/images'),
        ),
    ]
