# Generated by Django 3.2.9 on 2024-02-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0032_alter_employees_info_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_info',
            name='employeeid',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
