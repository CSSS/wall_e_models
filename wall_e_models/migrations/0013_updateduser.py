# Generated by Django 3.2.20 on 2023-11-13 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_e_models', '0012_auto_20231111_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdatedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_point', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wall_e_models.userpoint')),
            ],
        ),
    ]
