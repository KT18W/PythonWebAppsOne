# Generated by Django 4.1 on 2022-09-21 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='title',
            new_name='Hero',
        ),
    ]
