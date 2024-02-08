# Generated by Django 5.0.1 on 2024-02-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leavetype',
            field=models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('emergency', 'Emergency Leave'), ('study', 'Study Leave')], default='sick', max_length=25, null=True),
        ),
    ]