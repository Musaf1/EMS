# Generated by Django 3.2.9 on 2024-02-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0015_auto_20240212_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendace_info',
            name='absent_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendace_info',
            name='total_time',
            field=models.TextField(blank=True, default=True),
        ),
    ]