# Generated by Django 3.2.20 on 2023-11-18 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0015_auto_20231116_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoint',
            name='avatar_url',
        ),
        migrations.RemoveField(
            model_name='userpoint',
            name='avatar_url_message_id',
        ),
        migrations.RemoveField(
            model_name='userpoint',
            name='leveling_message_avatar_url',
        ),
        migrations.RemoveField(
            model_name='userpoint',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userpoint',
            name='nickname',
        ),
    ]
