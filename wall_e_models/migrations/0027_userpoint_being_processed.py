# Generated by Django 3.2.20 on 2025-03-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0026_userpoint_last_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoint',
            name='being_processed',
            field=models.BooleanField(default=False),
        ),
    ]
