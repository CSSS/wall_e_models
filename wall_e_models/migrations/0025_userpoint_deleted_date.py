# Generated by Django 3.2.20 on 2025-01-18 05:26

from django.db import migrations
import django.utils.timezone
import wall_e_models.customFields


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0024_userpoint_discord_avatar_link_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoint',
            name='deleted_date',
            field=wall_e_models.customFields.PSTDateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]