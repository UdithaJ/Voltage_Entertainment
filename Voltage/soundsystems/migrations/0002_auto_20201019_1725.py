# Generated by Django 3.0.8 on 2020-10-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundsystems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sound_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_name', models.CharField(max_length=500)),
                ('Suitable_for', models.CharField(max_length=500)),
                ('Brand', models.CharField(max_length=500)),
                ('Price', models.CharField(max_length=500)),
                ('Description', models.CharField(max_length=2500)),
            ],
            options={
                'db_table': 'soundsystem',
            },
        ),
        migrations.DeleteModel(
            name='sound_admin_upload',
        ),
    ]
