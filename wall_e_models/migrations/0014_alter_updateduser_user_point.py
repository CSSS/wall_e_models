# Generated by Django 3.2.23 on 2023-11-14 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0013_updateduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateduser',
            name='user_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wall_e_models.userpoint'),
        ),
    ]