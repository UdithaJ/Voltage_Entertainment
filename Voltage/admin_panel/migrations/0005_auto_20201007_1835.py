# Generated by Django 3.0.8 on 2020-10-07 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_bin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bin',
            new_name='eventbin',
        ),
    ]