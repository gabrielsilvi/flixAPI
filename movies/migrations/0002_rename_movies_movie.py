# Generated by Django 5.1 on 2024-11-14 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
        ('genres', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]