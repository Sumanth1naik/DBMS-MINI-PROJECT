# Generated by Django 4.1.5 on 2023-01-29 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gfg1', '0008_rename_innovaters_funders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organisation',
            new_name='Donaters',
        ),
    ]
