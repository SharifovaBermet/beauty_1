# Generated by Django 5.0.3 on 2024-03-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_services_options_alter_services_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
    ]