# Generated by Django 3.2.20 on 2023-08-31 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0007_auto_20230827_1520'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BanRecords',
            new_name='BanRecord',
        ),
    ]