# Generated by Django 3.2.9 on 2024-02-25 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0045_auto_20240225_2329'),
        ('leave', '0003_alter_leave_leavetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='Manger_approve_by',
            field=models.TextField(default='pending', max_length=100),
        ),
        migrations.AddField(
            model_name='leave',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leave',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]