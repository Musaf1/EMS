# Generated by Django 3.2.9 on 2024-02-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0023_auto_20240213_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees_info',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employees_info',
            name='employeeid',
            field=models.TextField(),
        ),
    ]
