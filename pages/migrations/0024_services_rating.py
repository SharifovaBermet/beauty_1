# Generated by Django 5.0 on 2024-05-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_services_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='rating',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Рейтинг услуги'),
        ),
    ]
