# Generated by Django 3.0.8 on 2020-10-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0013_auto_20201009_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
