# Generated by Django 4.1.13 on 2024-03-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='queue_info',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Очередь'),
        ),
    ]
