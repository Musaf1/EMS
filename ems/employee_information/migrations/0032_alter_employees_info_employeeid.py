# Generated by Django 3.2.9 on 2024-02-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0031_alter_employees_info_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_info',
            name='employeeid',
            field=models.TextField(),
        ),
    ]