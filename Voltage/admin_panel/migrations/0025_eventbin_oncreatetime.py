# Generated by Django 3.0.8 on 2020-10-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0024_auto_20201017_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventbin',
            name='OnCreateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
