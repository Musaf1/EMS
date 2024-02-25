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
    total_time = models.TextField(blank=True , default= True)
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
    start_perod = models.DateField(_('Date attended'),help_text='peroid start ',blank=False,null=True)
    end_perod = models.DateField(_('Date attended'),help_text='end of peroid',blank=False,null=True)
    
class payment(models.Model):
    name = models.ForeignKey(Employees_info, on_delete=models.CASCADE)
    other_payment = models.FloatField(default=0) 
    other_deduction = models.FloatField(default=0) 
    year_increase =  models.FloatField(default=0)
    