# Generated by Django 3.0.8 on 2020-10-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundsystems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound_admin_upload',
            name='Brand',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sound_admin_upload',
            name='Package_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sound_admin_upload',
            name='Price',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sound_admin_upload',
            name='Suitable_for',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sound_admin_upload',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
