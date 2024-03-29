# Generated by Django 3.2.20 on 2024-03-29 03:20

from django.db import migrations
import django.utils.timezone
import wall_e_models.customFields


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0023_auto_20240115_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoint',
            name='discord_avatar_link_expiry_date',
            field=wall_e_models.customFields.PSTDateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]