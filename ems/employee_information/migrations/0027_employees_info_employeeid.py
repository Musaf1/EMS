# Generated by Django 3.2.9 on 2024-02-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0026_remove_employees_info_employeeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees_info',
            name='employeeid',
            field=models.TextField(default=12345),
        ),
    ]