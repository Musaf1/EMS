# Generated by Django 3.2.9 on 2024-02-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0011_employees_info_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees_info',
            name='not_paid_hours',
            field=models.FloatField(default=0),
        ),
    ]