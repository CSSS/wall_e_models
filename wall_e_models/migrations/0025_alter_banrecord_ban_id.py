# Generated by Django 4.2.16 on 2024-10-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0024_userpoint_discord_avatar_link_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banrecord',
            name='ban_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]