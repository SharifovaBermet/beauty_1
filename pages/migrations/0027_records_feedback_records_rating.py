# Generated by Django 5.0 on 2024-05-06 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_branch_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='feedback',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='records',
            name='rating',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]