# Generated by Django 5.0.3 on 2024-03-09 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]