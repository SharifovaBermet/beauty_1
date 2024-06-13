# Generated by Django 5.0.3 on 2024-03-04 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Service_View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_view', to='pages.services')),
            ],
        ),
    ]
