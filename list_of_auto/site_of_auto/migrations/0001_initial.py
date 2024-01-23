# Generated by Django 5.0.1 on 2024-01-23 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_brand', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('user_mail', models.EmailField(max_length=254)),
                ('user_phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Automodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automodel', models.CharField(max_length=255)),
                ('autobrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_of_auto.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('FR', 'FREE'), ('USE', 'INUSE')], max_length=255)),
                ('vin_code', models.CharField(max_length=255)),
                ('automodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_of_auto.automodel')),
                ('autobrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_of_auto.brand')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_of_auto.usercar')),
            ],
        ),
    ]