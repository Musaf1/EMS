# Generated by Django 3.2.9 on 2024-02-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0047_alter_attendace_info_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendace_info',
            name='total_time',
            field=models.FloatField(),
        ),
    ]