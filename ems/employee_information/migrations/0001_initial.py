# Generated by Django 4.1.1 on 2024-02-22 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(blank=True, max_length=100)),
                ('name', models.TextField(unique=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact', models.TextField()),
                ('address', models.TextField()),
                ('email', models.TextField()),
                ('startdate', models.DateField(default=None, help_text='date of employement', null=True, verbose_name='Employement Date')),
                ('salary', models.FloatField(default=0)),
                ('gosi', models.FloatField(default=0)),
                ('deduction', models.FloatField(default=0)),
                ('total_salary', models.FloatField(default=0)),
                ('other_payment', models.FloatField(default=0)),
                ('other_deduction', models.FloatField(default=0)),
                ('bank_name', models.TextField(null=True)),
                ('acount_number', models.TextField(default=0, max_length=25)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('employeetype', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Intern', 'Intern')], default='Full-Time', max_length=15, null=True, verbose_name='Employee Type')),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.building_info')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.department_info')),
            ],
        ),
        migrations.CreateModel(
            name='Pirod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee', models.TextField()),
                ('start_perod', models.DateField(help_text='peroid start ', null=True, verbose_name='Date attended')),
                ('end_perod', models.DateField(help_text='end of peroid', null=True, verbose_name='Date attended')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_payment', models.FloatField(default=0)),
                ('other_deduction', models.FloatField(default=0)),
                ('year_increase', models.FloatField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info')),
            ],
        ),
        migrations.CreateModel(
            name='LinkUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='default.png', upload_to='images/')),
                ('is_blocked', models.BooleanField(default=False, help_text='button to toggle employee block and unblock', verbose_name='Is Blocked')),
                ('is_deleted', models.BooleanField(default=False, help_text='button to toggle employee deleted and undelete', verbose_name='Is Deleted')),
                ('dateissued', models.DateField(help_text='date staff id was issued', null=True, verbose_name='Date Issued')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employees_info',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.position'),
        ),
        migrations.CreateModel(
            name='Attendace_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='date staff Date attended', null=True, verbose_name='Date attended')),
                ('Time_attendace', models.TimeField(help_text='date staff Date attended', verbose_name='Date attended')),
                ('time_leaves', models.TimeField(help_text='date staff Date attended', verbose_name='Date attended')),
                ('total_time', models.TextField(blank=True, default=True)),
                ('absent_days', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info')),
            ],
        ),
    ]
