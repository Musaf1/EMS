# Generated by Django 3.2.9 on 2024-02-07 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0005_auto_20240207_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_info',
            name='contact',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='employees_info',
            name='name',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
