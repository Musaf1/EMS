from datetime import datetime
from django.db import models
from django.utils import timezone
from employee_information.utility import code_format


from employee_information.managers import EmployeeManager
#from phonenumber_field.modelfields import PhoneNumberField
#from django.utils.translation import ugettext as _ # virasoin 3.9
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from location_field.models.plain import PlainLocationField
#from leave.models import Leave



# Create your models here.


class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    # change data_added to create 
    created = models.DateTimeField(default=timezone.now) 
    # change data_update to update 
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Department_info(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    # change data_added to create 
    created = models.DateTimeField(default=timezone.now) 
    # change data_update to update 
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
class Building_info(models.Model):
    name = models.TextField(unique=True) 
    description = models.TextField() 
    status = models.IntegerField() 
    location = PlainLocationField(based_fields=['address'], zoom=7, default="26.377387, 50.011715")
    # change data_added to create 
    created = models.DateTimeField(default=timezone.now) 
    # change data_update to update 
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.location:
            self.location = "26.377387, 50.011715"
        super().save(*args, **kwargs)    
     
    
class Employees_info(models.Model):

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    NOT_KNOWN = 'Not Known'

    GENDER = (
    (MALE,'Male'),
    (FEMALE,'Female'),
    (OTHER,'Other'),
    (NOT_KNOWN,'Not Known'),
    )

    MR = 'Mr'
    MRS = 'Mrs'
    MSS = 'Mss'
    DR = 'Dr'
    SIR = 'Sir'
    MADAM = 'Madam'

    TITLE = (
    (MR,'Mr'),
    (MRS,'Mrs'),
    (MSS,'Mss'),
    (DR,'Dr'),
    (SIR,'Sir'),
    (MADAM,'Madam'),
    )


    FULL_TIME = 'Full-Time'
    PART_TIME = 'Part-Time'
    CONTRACT = 'Contract'
    INTERN = 'Intern'

    EMPLOYEETYPE = (
    (FULL_TIME,'Full-Time'),
    (PART_TIME,'Part-Time'),
    (CONTRACT,'Contract'),
    (INTERN,'Intern'),
    )

    
    Saudi = 'Saudi'
    Non_Sadui = 'Non-Sadui'

    NationalityType = (
    ('Andorra', _('Andorra')),
    ('United Arab Emirates', _('United Arab Emirates')),
    ('Afghanistan', _('Afghanistan')),
    ('Antigua & Barbuda', _('Antigua & Barbuda')),
    ('Anguilla', _('Anguilla')),
    ('Albania', _('Albania')),
    ('Armenia', _('Armenia')),
    ('Netherlands Antilles', _('Netherlands Antilles')),
    ('Angola', _('Angola')),
    ('Antarctica', _('Antarctica')),
    ('Argentina', _('Argentina')),
    ('American Samoa', _('American Samoa')),
    ('Austria', _('Austria')),
    ('Australia', _('Australia')),
    ('Aruba', _('Aruba')),
    ('Azerbaijan', _('Azerbaijan')),
    ('Bosnia and Herzegovina', _('Bosnia and Herzegovina')),
    ('Barbados', _('Barbados')),
    ('Bangladesh', _('Bangladesh')),
    ('Belgium', _('Belgium')),
    ('Burkina Faso', _('Burkina Faso')),
    ('Bulgaria', _('Bulgaria')),
    ('Bahrain', _('Bahrain')),
    ('Burundi', _('Burundi')),
    ('Benin', _('Benin')),
    ('Bermuda', _('Bermuda')),
    ('Brunei Darussalam', _('Brunei Darussalam')),
    ('Bolivia', _('Bolivia')),
    ('Brazil', _('Brazil')),
    ('Bahama', _('Bahama')),
    ('Bhutan', _('Bhutan')),
    ('Bouvet Island', _('Bouvet Island')),
    ('Botswana', _('Botswana')),
    ('Belarus', _('Belarus')),
    ('Belize', _('Belize')),
    ('Canada', _('Canada')),
    ('Cocos (Keeling) Islands', _('Cocos (Keeling) Islands')),
    ('Central African Republic', _('Central African Republic')),
    ('Congo', _('Congo')),
    ('Switzerland', _('Switzerland')),
    ('Ivory Coast', _('Ivory Coast')),
    ('Cook Iislands', _('Cook Iislands')),
    ('Chile', _('Chile')),
    ('Cameroon', _('Cameroon')),
    ('China', _('China')),
    ('Colombia', _('Colombia')),
    ('Costa Rica', _('Costa Rica')),
    ('Cuba', _('Cuba')),
    ('Cape Verde', _('Cape Verde')),
    ('Christmas Island', _('Christmas Island')),
    ('Cyprus', _('Cyprus')),
    ('Czech Republic', _('Czech Republic')),
    ('Germany', _('Germany')),
    ('Djibouti', _('Djibouti')),
    ('Denmark', _('Denmark')),
    ('Dominica', _('Dominica')),
    ('Dominican Republic', _('Dominican Republic')),
    ('Algeria', _('Algeria')),
    ('Ecuador', _('Ecuador')),
    ('Estonia', _('Estonia')),
    ('Egypt', _('Egypt')),
    ('Western Sahara', _('Western Sahara')),
    ('Eritrea', _('Eritrea')),
    ('Spain', _('Spain')),
    ('Ethiopia', _('Ethiopia')),
    ('Finland', _('Finland')),
    ('Fiji', _('Fiji')),
    ('Falkland Islands (Malvinas)', _('Falkland Islands (Malvinas)')),
    ('Micronesia', _('Micronesia')),
    ('Faroe Islands', _('Faroe Islands')),
    ('France', _('France')),
    ('France, Metropolitan', _('France, Metropolitan')),
    ('Gabon', _('Gabon')),
    ('United Kingdom (Great Britain)', _('United Kingdom (Great Britain)')),
    ('Grenada', _('Grenada')),
    ('Georgia', _('Georgia')),
    ('French Guiana', _('French Guiana')),
    ('Ghana', _('Ghana')),
    ('Gibraltar', _('Gibraltar')),
    ('Greenland', _('Greenland')),
    ('Gambia', _('Gambia')),
    ('Guinea', _('Guinea')),
    ('Guadeloupe', _('Guadeloupe')),
    ('Equatorial Guinea', _('Equatorial Guinea')),
    ('Greece', _('Greece')),
    ('South Georgia and the South Sandwich Islands', _('South Georgia and the South Sandwich Islands')),
    ('Guatemala', _('Guatemala')),
    ('Guam', _('Guam')),
    ('Guinea-Bissau', _('Guinea-Bissau')),
    ('Guyana', _('Guyana')),
    ('Hong Kong', _('Hong Kong')),
    ('Heard & McDonald Islands', _('Heard & McDonald Islands')),
    ('Honduras', _('Honduras')),
    ('Croatia', _('Croatia')),
    ('Haiti', _('Haiti')),
    ('Hungary', _('Hungary')),
    ('Indonesia', _('Indonesia')),
    ('Ireland', _('Ireland')),
    ('Israel', _('Israel')),
    ('India', _('India')),
    ('British Indian Ocean Territory', _('British Indian Ocean Territory')),
    ('Iraq', _('Iraq')),
    ('Islamic Republic of Iran', _('Islamic Republic of Iran')),
    ('Iceland', _('Iceland')),
    ('Italy', _('Italy')),
    ('Jamaica', _('Jamaica')),
    ('Jordan', _('Jordan')),
    ('Japan', _('Japan')),
    ('Kenya', _('Kenya')),
    ('Kyrgyzstan', _('Kyrgyzstan')),
    ('Cambodia', _('Cambodia')),
    ('Kiribati', _('Kiribati')),
    ('Comoros', _('Comoros')),
    ('St. Kitts and Nevis', _('St. Kitts and Nevis')),
    ('Korea, Democratic People\'s Republic of', _('Korea, Democratic People\'s Republic of')),
    ('Korea, Republic of', _('Korea, Republic of')),
    ('Kuwait', _('Kuwait')),
    ('Cayman Islands', _('Cayman Islands')),
    ('Kazakhstan', _('Kazakhstan')),
    ('Lao People\'s Democratic Republic', _('Lao People\'s Democratic Republic')),
    ('Lebanon', _('Lebanon')),
    ('Saint Lucia', _('Saint Lucia')),
    ('Liechtenstein', _('Liechtenstein')),
    ('Sri Lanka', _('Sri Lanka')),
    ('Liberia', _('Liberia')),
    ('Lesotho', _('Lesotho')),
    ('Lithuania', _('Lithuania')),
    ('Luxembourg', _('Luxembourg')),
    ('Latvia', _('Latvia')),
    ('Libyan Arab Jamahiriya', _('Libyan Arab Jamahiriya')),
    ('Morocco', _('Morocco')),
    ('Monaco', _('Monaco')),
    ('Moldova, Republic of', _('Moldova, Republic of')),
    ('Madagascar', _('Madagascar')),
    ('Marshall Islands', _('Marshall Islands')),
    ('Mali', _('Mali')),
    ('Mongolia', _('Mongolia')),
    ('Myanmar', _('Myanmar')),
    ('Macau', _('Macau')),
    ('Northern Mariana Islands', _('Northern Mariana Islands')),
    ('Martinique', _('Martinique')),
    ('Mauritania', _('Mauritania')),
    ('Monserrat', _('Monserrat')),
    ('Malta', _('Malta')),
    ('Mauritius', _('Mauritius')),
    ('Maldives', _('Maldives')),
    ('Malawi', _('Malawi')),
    ('Mexico', _('Mexico')),
    ('Malaysia', _('Malaysia')),
    ('Mozambique', _('Mozambique')),
    ('Namibia', _('Namibia')),
    ('New Caledonia', _('New Caledonia')),
    ('Niger', _('Niger')),
    ('Norfolk Island', _('Norfolk Island')),
    ('Nigeria', _('Nigeria')),
    ('Nicaragua', _('Nicaragua')),
    ('Netherlands', _('Netherlands')),
    ('Norway', _('Norway')),
    ('Nepal', _('Nepal')),
    ('Nauru', _('Nauru')),
    ('Niue', _('Niue')),
    ('New Zealand', _('New Zealand')),
    ('Oman', _('Oman')),
    ('Panama', _('Panama')),
    ('Peru', _('Peru')),
    ('French Polynesia', _('French Polynesia')),
    ('Papua New Guinea', _('Papua New Guinea')),
    ('Philippines', _('Philippines')),
    ('Pakistan', _('Pakistan')),
    ('Poland', _('Poland')),
    ('St. Pierre & Miquelon', _('St. Pierre & Miquelon')),
    ('Pitcairn', _('Pitcairn')),
    ('Puerto Rico', _('Puerto Rico')),
    ('Portugal', _('Portugal')),
    ('Palau', _('Palau')),
    ('Paraguay', _('Paraguay')),
    ('Qatar', _('Qatar')),
    ('Reunion', _('Reunion')),
    ('Romania', _('Romania')),
    ('Russian Federation', _('Russian Federation')),
    ('Rwanda', _('Rwanda')),
    ('Saudi', _('Saudi')),
    ('Solomon Islands', _('Solomon Islands')),
    ('Seychelles', _('Seychelles')),
    ('Sudan', _('Sudan')),
    ('Sweden', _('Sweden')),
    ('Singapore', _('Singapore')),
    ('St. Helena', _('St. Helena')),
    ('Slovenia', _('Slovenia')),
    ('Svalbard & Jan Mayen Islands', _('Svalbard & Jan Mayen Islands')),
    ('Slovakia', _('Slovakia')),
    ('Sierra Leone', _('Sierra Leone')),
    ('San Marino', _('San Marino')),
    ('Senegal', _('Senegal')),
    ('Somalia', _('Somalia')),
    ('Suriname', _('Suriname')),
    ('Sao Tome & Principe', _('Sao Tome & Principe')),
    ('El Salvador', _('El Salvador')),
    ('Syrian Arab Republic', _('Syrian Arab Republic')),
    ('Swaziland', _('Swaziland')),
    ('Turks & Caicos Islands', _('Turks & Caicos Islands')),
    ('Chad', _('Chad')),
    ('French Southern Territories', _('French Southern Territories')),
    ('Togo', _('Togo')),
    ('Thailand', _('Thailand')),
    ('Tajikistan', _('Tajikistan')),
    ('Tokelau', _('Tokelau')),
    ('Turkmenistan', _('Turkmenistan')),
    ('Tunisia', _('Tunisia')),
    ('Tonga', _('Tonga')),
    ('East Timor', _('East Timor')),
    ('Turkey', _('Turkey')),
    ('Trinidad & Tobago', _('Trinidad & Tobago')),
    ('Tuvalu', _('Tuvalu')),
    ('Taiwan, Province of China', _('Taiwan, Province of China')),
    ('Tanzania, United Republic of', _('Tanzania, United Republic of')),
    ('Ukraine', _('Ukraine')),
    ('Uganda', _('Uganda')),
    ('United States Minor Outlying Islands', _('United States Minor Outlying Islands')),
    ('United States of America', _('United States of America')),
    ('Uruguay', _('Uruguay')),
    ('Uzbekistan', _('Uzbekistan')),
    ('Vatican City State (Holy See)', _('Vatican City State (Holy See)')),
    ('St. Vincent & the Grenadines', _('St. Vincent & the Grenadines')),
    ('Venezuela', _('Venezuela')),
    ('British Virgin Islands', _('British Virgin Islands')),
    ('United States Virgin Islands', _('United States Virgin Islands')),
    ('Viet Nam', _('Viet Nam')),
    ('Vanuatu', _('Vanuatu')),
    ('Wallis & Futuna Islands', _('Wallis & Futuna Islands')),
    ('Samoa', _('Samoa')),
    ('Yemen', _('Yemen')),
    ('Mayotte', _('Mayotte')),
    ('Yugoslavia', _('Yugoslavia')),
    ('South Africa', _('South Africa')),
    ('Zambia', _('Zambia')),
    ('Zaire', _('Zaire')),
    ('Zimbabwe', _('Zimbabwe')),
)


    # change code to employeeid
    employeeid = models.CharField(max_length=100,blank=True)
    name = models.TextField(unique=True) 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    # change department_id to department
    department = models.ForeignKey(Department_info, on_delete=models.CASCADE )  
    # change position_id to position
    position = models.ForeignKey(Position, on_delete=models.CASCADE) 
    build = models.ForeignKey(Building_info, on_delete=models.CASCADE) 
    startdate = models.DateField(_('Employement Date'),help_text='date of employement',blank=False,null=True , default = None) 
    salary = models.FloatField(default=0) 
    gosi = models.FloatField(default=0) 
    deduction = models.FloatField(default=0)
    total_salary = models.FloatField(default=0) 
    other_payment = models.FloatField(default=0) 
    other_deduction = models.FloatField(default=0) 
    bank_name = models.TextField(null= True) 
    acount_number = models.TextField(max_length = 25, default=0)
    status = models.IntegerField() 
    #change date_added to created
    created = models.DateTimeField(auto_now_add=True) 
    #change data_update to updated
    updated = models.DateTimeField(auto_now_add=True) 
    employeetype = models.CharField(_('Employee Type'),max_length=15,default=FULL_TIME,choices=EMPLOYEETYPE,blank=False,null=True)
    Nationality = models.CharField(max_length=50, choices=NationalityType,blank=False,null= True) 
    
    def save(self,*args,**kwargs):
        '''
        overriding the save method - for every instance that calls the save method 
        perform this action on its employee_id
        

        '''
        get_id = self.employeeid #grab employee_id number from submitted form field
        data = code_format(get_id)
        self.employeeid = data #pass the new code to the employee_id as its orifinal or actual code
        super().save(*args,**kwargs) # call the parent save method
        # print(self.employeeid)
    
    def __str__(self):
        return self.name 
#class

class Attendace_info(models.Model):
    name = models.ForeignKey(Employees_info, on_delete=models.CASCADE )  
    #name = models.TextField()
    date = models.DateField(_('Date attended'),help_text='date staff Date attended',blank=False,null=True)
    Time_attendace = models.TimeField(_('Date attended'),help_text='date staff Date attended')
    time_leaves = models.TimeField(_('Date attended'),help_text='date staff Date attended')
    total_time = models.FloatField()
    absent_days = models.IntegerField(default=0)


class LinkUser(models.Model):
    # add reson
    user = models.OneToOneField(User , null=True , on_delete=models.CASCADE)
    # employeeid = models.OneToOneField(Employees_info, on_delete=models.CASCADE)
    name = models.ForeignKey(Employees_info, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/',default='default.png')#work on path username-date/image
    is_blocked = models.BooleanField(_('Is Blocked'),help_text='button to toggle employee block and unblock',default=False)
    is_deleted = models.BooleanField(_('Is Deleted'),help_text='button to toggle employee deleted and undelete',default=False)
    dateissued = models.DateField(_('Date Issued'),help_text='date staff id was issued',blank=False,null=True)

    # #PLUG MANAGERS
    # objects = EmployeeManager()

    
    # class Meta:
    #     verbose_name = _('Employee')
    #     verbose_name_plural = _('Employees')
    #     #ordering = ['-created']



    # def __str__(self):
    #     return self.get_full_name

    

    # @property
    # def get_full_name(self):
    #     fullname = ''
    #     firstname = self.firstname
    #     lastname = self.lastname
    #     othername = self.othername

    #     if (firstname and lastname) or othername is None:
    #         fullname = firstname +' '+ lastname
    #         return fullname
    #     elif othername:
    #         fullname = firstname + ' '+ lastname +' '+othername
    #         return fullname
    #     return


    # @property
    # def get_age(self):
    #     current_year = datetime.date.today().year
    #     dateofbirth_year = self.birthday.year
    #     if dateofbirth_year:
    #         return current_year - dateofbirth_year
    #     return



    # @property
    # def can_apply_leave(self):
    #     pass
    
    
class Pirod(models.Model):
    #Employee = models.ForeignKey(Employees_info, on_delete=models.CASCADE)
    Employee = models.TextField() 
    start_perod = models.DateField(_('Date attended'),help_text='peroid start ',blank=False,null=True)
    end_perod = models.DateField(_('Date attended'),help_text='end of peroid',blank=False,null=True)
    
class payment(models.Model):
    name = models.ForeignKey(Employees_info, on_delete=models.CASCADE)
    other_payment = models.FloatField(default=0) 
    other_deduction = models.FloatField(default=0) 
    year_increase =  models.FloatField(default=0)
    