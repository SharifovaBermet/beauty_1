# Generated by Django 5.0 on 2024-05-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_alter_movement_options_master_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='feedback_rev',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]