from django.db import models
from .manager import LeaveManager
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from employee_information.models import Employees_info


# Create your models here.

# types of leaves requsts , added in filed down as choises, so user can chose which type of leaves he want 
SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
STUDY = 'study'

LEAVE_TYPE = (
(SICK,'Sick Leave'),
(CASUAL,'Casual Leave'),
(EMERGENCY,'Emergency Leave'),
(STUDY,'Study Leave') )

DAYS = 30


class Leave(models.Model):
	name = models.ForeignKey(Employees_info,on_delete=models.CASCADE,default=1)
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	startdate = models.DateField(verbose_name=_('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
	enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
	leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=SICK,null=True,blank=False)
	reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)
	defaultdays = models.PositiveIntegerField(verbose_name=_('Leave days per year counter'),default=DAYS,null=True,blank=True)



	status = models.CharField(max_length=100,default='pending') #pending,approved,rejected,cancelled
	is_approved = models.BooleanField(default=False) #hide
	Manger_approve_by = models.TextField(max_length=100,default='pending') #pending,approved,rejected,cancelled

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	counter = models.IntegerField(default = 0)

	objects = LeaveManager()


	class Meta:
		verbose_name = _('Leave')
		verbose_name_plural = _('Leaves')
		ordering = ['-created'] #recent objects



	def __str__(self):
		return ('{0} - {1}'.format(self.leavetype,self.user))




	@property
	def pretty_leave(self):
		leave = self.leavetype
		user = self.user
		employee = user.employee_set.first().get_full_name
		return ('{0} - {1}'.format(employee,leave))



	@property
	def leave_days(self):
		days_count = ''
		startdate = self.startdate
		enddate = self.enddate
		"""if startdate > enddate:
			return
		"""	
		dates = (enddate - startdate)
		return dates.days



	@property
	def leave_approved(self):
		return self.is_approved == True




	@property
	def approve_leave(self):
		
		#if not self.is_approved:
		
		if self.counter == 0:
			self.counter = 1
			print("fisrt if, self.counter : ",self.counter)
			self.Manger_approve_by = "approved by Department Manger"
			self.status = 'pending'	
		else:
			self.is_approved = True
			self.counter = 2
			self.Manger_approve_by = "approved"
			print("second if,self.counter : ",self.counter)
			self.status = 'approved'
		self.save()





	@property
	def unapprove_leave(self):
		if self.counter <= 1:
			self.counter = 0
			self.is_approved = False
			print("fisrt if, self.counter : ",self.counter)
			self.Manger_approve_by = "pending"
			self.status = 'pending'	
		else:
			self.counter = 1
			self.is_approved = False
			self.Manger_approve_by = " approved by Department Manger "
			self.status = 'pending'
			print("second if,self.counter : ",self.counter)
			self.save()
			
			
			



	@property
	def leaves_cancel(self):
		if self.is_approved or not self.is_approved:
			self.counter = 0
			self.is_approved = False
			self.Manger_approve_by = "cancelled"
			self.status = 'cancelled'
			self.save()






	@property
	def reject_leave(self):
		if self.is_approved or not self.is_approved:
			self.counter = 0
			self.is_approved = False
			self.Manger_approve_by = "rejected"
			self.status = 'rejected'
			self.save()



	@property
	def is_rejected(self):
		return self.status == 'rejected'



