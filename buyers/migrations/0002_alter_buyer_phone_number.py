# Generated by Django 5.1.2 on 2024-11-03 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Введите корректный номер телефона (например, +79991234567).', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
