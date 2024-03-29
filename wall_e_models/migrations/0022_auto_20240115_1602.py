# Generated by Django 3.2.20 on 2024-01-16 00:02

from django.db import migrations
import wall_e_models.customFields


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0021_alter_banrecord_is_purged'),
    ]

    operations = [
        migrations.AddField(
            model_name='banrecord',
            name='ban_date',
            field=wall_e_models.customFields.PSTDateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='banrecord',
            name='unban_date',
            field=wall_e_models.customFields.PSTDateTimeField(default=None, null=True),
        ),
    ]
