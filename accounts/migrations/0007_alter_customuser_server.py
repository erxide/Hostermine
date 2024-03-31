# Generated by Django 5.0.3 on 2024-03-13 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_server'),
        ('minecraft', '0007_remove_server_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='minecraft.server'),
        ),
    ]
