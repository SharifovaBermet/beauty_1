# Generated by Django 4.1.13 on 2024-03-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_delete_applications_alter_records_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='date_rec_info',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]