# Generated by Django 3.0.8 on 2020-10-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0020_events_oncreatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='OnCreateTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
