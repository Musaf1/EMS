# Generated by Django 3.2.9 on 2024-02-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0046_merge_20240226_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendace_info',
            name='total_time',
            field=models.IntegerField(),
        ),
    ]
