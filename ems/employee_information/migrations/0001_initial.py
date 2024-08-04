# Generated by Django 5.0.2 on 2024-08-04 14:36

import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain
from django.conf import settings
from django.db import migrations, models


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
                ('name', models.TextField(unique=True)),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('location', location_field.models.plain.PlainLocationField(default='26.377387, 50.011715', max_length=63)),
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
                ('Nationality', models.CharField(choices=[('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Afghanistan', 'Afghanistan'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Anguilla', 'Anguilla'), ('Albania', 'Albania'), ('Armenia', 'Armenia'), ('Netherlands Antilles', 'Netherlands Antilles'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('American Samoa', 'American Samoa'), ('Austria', 'Austria'), ('Australia', 'Australia'), ('Aruba', 'Aruba'), ('Azerbaijan', 'Azerbaijan'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Barbados', 'Barbados'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Burkina Faso', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'), ('Bahama', 'Bahama'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Central African Republic', 'Central African Republic'), ('Congo', 'Congo'), ('Switzerland', 'Switzerland'), ('Ivory Coast', 'Ivory Coast'), ('Cook Iislands', 'Cook Iislands'), ('Chile', 'Chile'), ('Cameroon', 'Cameroon'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Cape Verde', 'Cape Verde'), ('Christmas Island', 'Christmas Island'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('Western Sahara', 'Western Sahara'), ('Eritrea', 'Eritrea'), ('Spain', 'Spain'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('Micronesia', 'Micronesia'), ('Faroe Islands', 'Faroe Islands'), ('France', 'France'), ('France, Metropolitan', 'France, Metropolitan'), ('Gabon', 'Gabon'), ('United Kingdom (Great Britain)', 'United Kingdom (Great Britain)'), ('Grenada', 'Grenada'), ('Georgia', 'Georgia'), ('French Guiana', 'French Guiana'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greenland', 'Greenland'), ('Gambia', 'Gambia'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Guatemala', 'Guatemala'), ('Guam', 'Guam'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard & McDonald Islands', 'Heard & McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Iraq', 'Iraq'), ('Islamic Republic of Iran', 'Islamic Republic of Iran'), ('Iceland', 'Iceland'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Comoros', 'Comoros'), ('St. Kitts and Nevis', 'St. Kitts and Nevis'), ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"), ('Korea, Republic of', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ('Cayman Islands', 'Cayman Islands'), ('Kazakhstan', 'Kazakhstan'), ("Lao People's Democratic Republic", "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Liberia', 'Liberia'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Marshall Islands', 'Marshall Islands'), ('Mali', 'Mali'), ('Mongolia', 'Mongolia'), ('Myanmar', 'Myanmar'), ('Macau', 'Macau'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Monserrat', 'Monserrat'), ('Malta', 'Malta'), ('Mauritius', 'Mauritius'), ('Maldives', 'Maldives'), ('Malawi', 'Malawi'), ('Mexico', 'Mexico'), ('Malaysia', 'Malaysia'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Philippines', 'Philippines'), ('Pakistan', 'Pakistan'), ('Poland', 'Poland'), ('St. Pierre & Miquelon', 'St. Pierre & Miquelon'), ('Pitcairn', 'Pitcairn'), ('Puerto Rico', 'Puerto Rico'), ('Portugal', 'Portugal'), ('Palau', 'Palau'), ('Paraguay', 'Paraguay'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saudi', 'Saudi'), ('Solomon Islands', 'Solomon Islands'), ('Seychelles', 'Seychelles'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Singapore', 'Singapore'), ('St. Helena', 'St. Helena'), ('Slovenia', 'Slovenia'), ('Svalbard & Jan Mayen Islands', 'Svalbard & Jan Mayen Islands'), ('Slovakia', 'Slovakia'), ('Sierra Leone', 'Sierra Leone'), ('San Marino', 'San Marino'), ('Senegal', 'Senegal'), ('Somalia', 'Somalia'), ('Suriname', 'Suriname'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('El Salvador', 'El Salvador'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Swaziland', 'Swaziland'), ('Turks & Caicos Islands', 'Turks & Caicos Islands'), ('Chad', 'Chad'), ('French Southern Territories', 'French Southern Territories'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('East Timor', 'East Timor'), ('Turkey', 'Turkey'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tuvalu', 'Tuvalu'), ('Taiwan, Province of China', 'Taiwan, Province of China'), ('Tanzania, United Republic of', 'Tanzania, United Republic of'), ('Ukraine', 'Ukraine'), ('Uganda', 'Uganda'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('United States of America', 'United States of America'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vatican City State (Holy See)', 'Vatican City State (Holy See)'), ('St. Vincent & the Grenadines', 'St. Vincent & the Grenadines'), ('Venezuela', 'Venezuela'), ('British Virgin Islands', 'British Virgin Islands'), ('United States Virgin Islands', 'United States Virgin Islands'), ('Viet Nam', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis & Futuna Islands', 'Wallis & Futuna Islands'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('Mayotte', 'Mayotte'), ('Yugoslavia', 'Yugoslavia'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zaire', 'Zaire'), ('Zimbabwe', 'Zimbabwe')], max_length=50, null=True)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.building_info')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.department_info')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.position')),
            ],
        ),
        migrations.CreateModel(
            name='Attendace_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='date staff Date attended', null=True, verbose_name='Date attended')),
                ('Time_attendace', models.TimeField(help_text='date staff Date attended', verbose_name='Date attended')),
                ('time_leaves', models.TimeField(help_text='date staff Date attended', verbose_name='Date attended')),
                ('total_time', models.FloatField()),
                ('absent_days', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info')),
            ],
        ),
        migrations.CreateModel(
            name='LinkUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='default.png', upload_to='images/')),
                ('mac', models.CharField(blank=True, max_length=150, verbose_name='mac')),
                ('change_mac', models.IntegerField(default=0, verbose_name='hange_mac')),
                ('is_blocked', models.BooleanField(default=False, help_text='button to toggle employee block and unblock', verbose_name='Is Blocked')),
                ('is_deleted', models.BooleanField(default=False, help_text='button to toggle employee deleted and undelete', verbose_name='Is Deleted')),
                ('dateissued', models.DateField(help_text='date staff id was issued', null=True, verbose_name='Date Issued')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees_info')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
    ]
