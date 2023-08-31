# Generated by Django 3.2.20 on 2023-08-27 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WalleModels', '0006_auto_20220909_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandstat',
            name='day',
            field=models.IntegerField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commandstat',
            name='hour',
            field=models.IntegerField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commandstat',
            name='month',
            field=models.IntegerField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commandstat',
            name='year',
            field=models.IntegerField(default=django.utils.timezone.now),
        ),
    ]