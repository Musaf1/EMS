# Generated by Django 3.2.9 on 2024-02-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0040_remove_employees_info_not_paid_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building_info',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]