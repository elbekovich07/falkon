# Generated by Django 5.1.7 on 2025-03-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customer_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
