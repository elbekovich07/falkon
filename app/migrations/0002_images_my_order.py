# Generated by Django 5.1.7 on 2025-03-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
