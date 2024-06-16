# Generated by Django 5.0.4 on 2024-04-11 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('species', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=100)),
                ('disability', models.CharField(blank=True, max_length=255)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pets')),
                ('allergies', models.CharField(blank=True, max_length=255)),
                ('availability', models.BooleanField(default=True)),
                ('gender', models.CharField(max_length=50)),
                ('health_status', models.CharField(max_length=100)),
                ('videos', models.FileField(blank=True, null=True, upload_to='pet_videos')),
                ('shelter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='PetAdoption.shelter')),
            ],
        ),
    ]
