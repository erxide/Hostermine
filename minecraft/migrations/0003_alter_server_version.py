# Generated by Django 5.0.3 on 2024-03-09 09:21

import django.db.models.deletion
import minecraft.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0002_version_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='version',
            field=models.ForeignKey(default=minecraft.models.get_last_version, null=True, on_delete=django.db.models.deletion.SET_NULL, to='minecraft.version'),
        ),
    ]