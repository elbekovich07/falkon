# Generated by Django 5.1.7 on 2025-03-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
            preserve_default=False,
        ),
    ]
