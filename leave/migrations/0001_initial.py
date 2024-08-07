# Generated by Django 5.0.2 on 2024-08-04 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(help_text='leave start date is on ..', null=True, verbose_name='Start Date')),
                ('enddate', models.DateField(help_text='coming back on ...', null=True, verbose_name='End Date')),
                ('leavetype', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('emergency', 'Emergency Leave'), ('study', 'Study Leave'), ('task', 'Task Leave')], default='sick', max_length=25, null=True)),
                ('reason', models.CharField(blank=True, help_text='add additional information for leave', max_length=255, null=True, verbose_name='Reason for Leave')),
                ('defaultdays', models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='Leave days per year counter')),
                ('status', models.CharField(default='pending', max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('Manger_approve_by', models.TextField(default='pending', max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('counter', models.IntegerField(default=0)),
                ('name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'ordering': ['-created'],
            },
        ),
    ]
