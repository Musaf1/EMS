# Generated by Django 4.2.4 on 2023-09-05 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_information', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='default.png', help_text='upload image size less than 2.0MB', null=True, upload_to='profiles', verbose_name='Profile Image')),
                ('startdate', models.DateField(help_text='date of employement', null=True, verbose_name='Employement Date')),
                ('dateissued', models.DateField(help_text='date staff id was issued', null=True, verbose_name='Date Issued')),
                ('is_blocked', models.BooleanField(default=False, help_text='button to toggle employee block and unblock', verbose_name='Is Blocked')),
                ('is_deleted', models.BooleanField(default=False, help_text='button to toggle employee deleted and undelete', verbose_name='Is Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_information.department', verbose_name='Department')),
                ('name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-created'],
            },
        ),
    ]
