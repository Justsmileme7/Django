# Generated by Django 5.0.1 on 2024-01-30 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_of_auto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='user',
        ),
        migrations.AddField(
            model_name='usercar',
            name='auto',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_of_auto.auto'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image_brand',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='logos'),
        ),
    ]