# Generated by Django 5.0.3 on 2024-03-13 20:28

import django.core.validators
import minecraft.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0008_server_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='port',
            field=models.IntegerField(blank=True, default=minecraft.models.get_port, validators=[django.core.validators.MaxValueValidator(26565), django.core.validators.MinValueValidator(25565)]),
        ),
    ]
