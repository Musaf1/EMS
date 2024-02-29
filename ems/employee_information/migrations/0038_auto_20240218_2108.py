# Generated by Django 3.2.9 on 2024-02-18 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0037_alter_linkuser_options'),
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
        migrations.RemoveField(
            model_name='department_info',
            name='location',
        ),
        migrations.AlterField(
            model_name='employees_info',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.building_info'),
        ),
        migrations.DeleteModel(
            name='Shift',
        ),
    ]
