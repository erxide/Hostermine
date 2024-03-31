# Generated by Django 5.0.3 on 2024-03-09 09:10

import django.core.validators
import django.db.models.deletion
import minecraft.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Difficulty',
                'verbose_name_plural': 'Difficulties',
            },
        ),
        migrations.CreateModel(
            name='gamemode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Gamemode',
                'verbose_name_plural': 'Gamemodes',
            },
        ),
        migrations.CreateModel(
            name='version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Version',
                'verbose_name_plural': 'Versions',
            },
        ),
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Minecraft Server', max_length=100)),
                ('max_players', models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('whitelist_enabled', models.BooleanField(default=False)),
                ('whitelist', models.JSONField(default=minecraft.models.default_whitelist)),
                ('online_mode', models.BooleanField(default=True)),
                ('pvp_enabled', models.BooleanField(default=True)),
                ('command_block_enabled', models.BooleanField(default=False)),
                ('allow_flight', models.BooleanField(default=False)),
                ('spawn_animals', models.BooleanField(default=True)),
                ('spawn_monsters', models.BooleanField(default=True)),
                ('spawn_npcs', models.BooleanField(default=True)),
                ('allow_nether', models.BooleanField(default=True)),
                ('force_gamemode', models.BooleanField(default=False)),
                ('spawn_protection', models.IntegerField(default=16, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('difficulty_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='minecraft.difficulty')),
                ('gamemode_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='minecraft.gamemode')),
                ('version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='minecraft.version')),
            ],
            options={
                'verbose_name': 'Server',
                'verbose_name_plural': 'Servers',
            },
        ),
    ]