# Generated by Django 3.2.23 on 2023-11-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0014_alter_updateduser_user_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoint',
            name='deleted_member',
        ),
        migrations.RemoveField(
            model_name='userpoint',
            name='leveling_update_needed',
        ),
        migrations.AddField(
            model_name='userpoint',
            name='date_to_check',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
