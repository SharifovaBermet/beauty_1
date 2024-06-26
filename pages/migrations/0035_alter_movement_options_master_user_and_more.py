# Generated by Django 5.0 on 2024-05-28 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_records_master_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movement',
            options={'verbose_name': 'Движения', 'verbose_name_plural': 'Движения'},
        ),
        migrations.AddField(
            model_name='master',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_info_mov', to=settings.AUTH_USER_MODEL, verbose_name='Выберите пользователя'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movement', to=settings.AUTH_USER_MODEL, verbose_name='Выберите пользователя'),
        ),
    ]
