# Generated by Django 3.2.23 on 2024-01-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0019_auto_20240114_2025'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='banrecord',
            constraint=models.UniqueConstraint(condition=models.Q(('epoch_unban_date__isnull', True)), fields=('user_id',), name='unique_active_ban'),
        ),
    ]