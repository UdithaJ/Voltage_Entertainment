# Generated by Django 3.0.8 on 2020-10-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0025_eventbin_oncreatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='Resources_Name',
            field=models.CharField(default='R', max_length=20),
            preserve_default=False,
        ),
    ]
