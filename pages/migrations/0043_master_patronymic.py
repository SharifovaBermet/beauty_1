# Generated by Django 5.0.3 on 2024-06-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0042_alter_salons_options_remove_master_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='patronymic',
            field=models.CharField(default=1, max_length=255, verbose_name='Отчество'),
            preserve_default=False,
        ),
    ]
