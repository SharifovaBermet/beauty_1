# Generated by Django 5.0 on 2024-05-23 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_alter_records_options_alter_records_date_rec_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='time_info',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
