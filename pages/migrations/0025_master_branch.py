# Generated by Django 5.0 on 2024-05-05 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_services_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_master', to='pages.branch', verbose_name='Филиал'),
        ),
    ]
