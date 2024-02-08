# Generated by Django 3.2.9 on 2024-02-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0009_employees_info_employeeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
    ]