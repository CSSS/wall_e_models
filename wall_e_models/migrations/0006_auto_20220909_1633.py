# Generated by Django 3.2.14 on 2022-09-09 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0004_auto_20220206_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoint',
            name='hidden',
            field=models.BooleanField(default=False),
        )
    ]
