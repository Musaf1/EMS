from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from employee.forms import EmployeeCreateForm
from leave.models import Leave
from employee.models import *
from employee_information.models import *
from leave.forms import LeaveCreationForm
from django.contrib.auth.decorators import login_required
from employee_information.forms import EmployeeCreateForm , LinkUserForm



# user must be loged in 
@login_required(login_url='accounts:login')
def dashboard(request):
	
	'''
	Summary of all apps - display here with charts etc.
	eg.lEAVE - PENDING|APPROVED|RECENT|REJECTED - TOTAL THIS MONTH or NEXT MONTH
	EMPLOYEE - TOTAL | GENDER 
	CHART - AVERAGE EMPLOYEE AGES
	'''
	dataset = dict()
	user = request.user

	if not request.user.is_authenticated:
		return redirect('accounts:login')

	employees = Employee.objects.all()
	leaves = Leave.objects.all_pending_leaves()
	
	staff_leaves = Leave.objects.filter(user = user)

	
	dataset['employees'] = employees
	dataset['leaves'] = leaves
	
	dataset['staff_leaves'] = staff_leaves
	dataset['title'] = 'summary'
	

	return render(request,'dashboard/dashboard_index.html',dataset)



@login_required(login_url='accounts:login')
def dashboard_employees(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')

	dataset = dict()
	departments = Department.objects.all()
	employees = Employee.objects.all()

	#pagination
	query = request.GET.get('search')
	if query:
		employees = employees.filter(
			Q(firstname__icontains = query) |
			Q(lastname__icontains = query)
		)



	paginator = Paginator(employees, 10) #show 10 employee lists per page

	page = request.GET.get('page')
	employees_paginated = paginator.get_page(page)



	blocked_employees = Employee.objects.all_blocked_employees()


	return render(request,'dashboard/employee_app.html',dataset)



@login_required(login_url='accounts:login')
def dashboard_employees_create(request):
	if not (request.user.is_authenticated and request.user.is_superuser):
		return redirect('/')

	if request.method == 'POST':
		form = LinkUserForm(request.POST,request.FILES)
		if form.is_valid():
			"""
			instance = form.save(commit = False)
			user = request.POST.get('user')
			assigned_user = User.objects.get(id = user)

			instance.user = assigned_user

			instance.title = request.POST.get('title')
			instance.image = request.FILES.get('image')
			instance.firstname = request.POST.get('firstname')
			instance.lastname = request.POST.get('lastname')
			instance.othername = request.POST.get('othername')
			
			instance.birthday = request.POST.get('birthday')

			

			



			role = request.POST.get('role')
			role_instance = Role.objects.get(id = role)
			instance.role = role_instance

			instance.startdate = request.POST.get('startdate')
			instance.employeetype = request.POST.get('employeetype')
			instance.employeeid = request.POST.get('employeeid')
			instance.dateissued = request.POST.get('dateissued')

			

			instance.save()

			

			return  redirect('dashboard:employees')
		else:
			messages.error(request,'Trying to create dublicate employees with a single user account ',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('dashboard:employeecreate')


	dataset = dict()
	form = EmployeeCreateForm()
	dataset['form'] = form
	dataset['title'] = 'register employee'
	return render(request,'dashboard/employee_create.html',dataset)

	"""
			instance = form.save(commit = False)
			user = request.POST.get('user')
			assigned_user = User.objects.get(id = user)

			instance.user = assigned_user

			instance.image = request.FILES.get('image')
	

			

			instance.save()


			

			return  redirect('dashboard:employees')
		else:
			messages.error(request,'Trying to create dublicate employees with a single user account ',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('dashboard:employeecreate')


	dataset = dict()
	form = LinkUserForm()
	dataset['form'] = form
	dataset['title'] = 'register employee'
	return render(request,'dashboard/employee_create.html',dataset)


	
@login_required(login_url='accounts:login')
def employee_edit_data(request,id):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	employee = get_object_or_404(Employee, id = id)
	if request.method == 'POST':
		form = EmployeeCreateForm(request.POST or None,request.FILES or None,instance = employee)
		if form.is_valid():
			instance = form.save(commit = False)

			user = request.POST.get('user')
			assigned_user = User.objects.get(id = user)

			instance.user = assigned_user

			instance.image = request.FILES.get('image')
			instance.firstname = request.POST.get('firstname')
			instance.lastname = request.POST.get('lastname')
			instance.othername = request.POST.get('othername')
			
			instance.birthday = request.POST.get('birthday')

			religion_id = request.POST.get('religion')
			religion = Religion.objects.get(id = religion_id)
			instance.religion = religion

			nationality_id = request.POST.get('nationality')
			nationality = Nationality.objects.get(id = nationality_id)
			instance.nationality = nationality

			department_id = request.POST.get('department')
			department = Department.objects.get(id = department_id)
			instance.department = department


			instance.hometown = request.POST.get('hometown')
			instance.region = request.POST.get('region')
			instance.residence = request.POST.get('residence')
			instance.address = request.POST.get('address')
			instance.education = request.POST.get('education')
			instance.lastwork = request.POST.get('lastwork')
			instance.position = request.POST.get('position')
			instance.ssnitnumber = request.POST.get('ssnitnumber')
			instance.tinnumber = request.POST.get('tinnumber')

			role = request.POST.get('role')
			role_instance = Role.objects.get(id = role)
			instance.role = role_instance

			instance.startdate = request.POST.get('startdate')
			instance.employeetype = request.POST.get('employeetype')
			instance.employeeid = request.POST.get('employeeid')
			instance.dateissued = request.POST.get('dateissued')

			# now = datetime.datetime.now()
			# instance.created = now
			# instance.updated = now

			instance.save()
			messages.success(request,'Account Updated Successfully !!!',extra_tags = 'alert alert-info alert-dismissible show')
			return redirect('dashboard:employees')

		else:

			messages.error(request,'Error Updating account',extra_tags = 'alert alert-warning alert-dismissible show')
			return HttpResponse("Form data not valid")

	dataset = dict()
	form = EmployeeCreateForm(request.POST or None,request.FILES or None,instance = employee)
	dataset['form'] = form
	dataset['title'] = 'edit - {0}'.format(employee.get_full_name)
	return render(request,'dashboard/employee_create.html',dataset)





@login_required(login_url='accounts:login')
def dashboard_employee_info(request,id):
	if not request.user.is_authenticated:
		return redirect('/')
	
	employee = get_object_or_404(Employee, id = id)
	
	
	dataset = dict()
	dataset['employee'] = employee
	dataset['title'] = 'profile - {0}'.format(employee.get_full_name)
	return render(request,'dashboard/employee_detail.html',dataset)






# ---------------------LEAVE-------------------------------------------


@login_required(login_url='accounts:login')
def leave_creation(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	if request.method == 'POST':
		form = LeaveCreationForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user_name = request.user
			#appled_name = get_object_or_404(LinkUser, user = user_name)
			#attendace_list = Attendace_info.objects.filter(name = employee_name )


			applyed2 = LinkUser.objects.filter(user = user_name).first()
			print("request.user : ",applyed2.name)
			'''
			user_id = request.user.id
			x = LinkUser.objects.filter(name = user)
			print("user : ", user_id)
			print("	LinkUser.name: ",LinkUser.name[])
			#name = request.name
			#print("name : ", name)
			'''
			instance.user = user_name
			instance.name = applyed2.name
 
			#instance.name = name
			instance.save()


			# print(instance.defaultdays)
			messages.success(request,'Leave Request Sent,wait for Admins response',extra_tags = 'alert alert-info alert-dismissible show')
			return redirect('dashboard:createleave')

		messages.error(request,'failed to Request a Leave,please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('dashboard:createleave')


	dataset = dict()
	form = LeaveCreationForm()
	dataset['form'] = form
	dataset['title'] = 'Apply for Leave'
	return render(request,'dashboard/create_leave.html',dataset)
	






@login_required(login_url='accounts:login')
def leaves_list(request):
	if not (request.user.is_staff or request.user.is_superuser):
		return redirect('/')
	leaves = Leave.objects.all_pending_leaves()
	employees = LinkUser.objects.all()
	return render(request,'dashboard/leaves_recent.html',{'leave_list':leaves, 'employees':employees ,'title':'leaves list - pending'})


@login_required(login_url='accounts:login')
def leaves_approved_list(request):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leaves = Leave.objects.all_approved_leaves() #approved leaves -> calling model manager method
	return render(request,'dashboard/leaves_approved.html',{'leave_list':leaves,'title':'approved leave list'})


# @login_required(login_url='accounts:login')
# def leaves_view(request,id):
# 	if not (request.user.is_authenticated):
# 		return redirect('/')

# 	leave = get_object_or_404(Leave, id = id)
# 	print(leave.user)
# 	employee = Employee.objects.filter(user = leave.user)[0]
# 	print(employee)
# 	return render(request,'dashboard/leave_detail_view.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})

@login_required(login_url='accounts:login')
def leaves_view(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')
	
	leave = get_object_or_404(Leave, id = id)
	employee = LinkUser.objects.filter(name = leave.name)[0]
	return render(request,'dashboard/leave_detail_view.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})


@login_required(login_url='accounts:login')
def approve_leave(request,id):
	if not (request.user.is_superuser or request.user.is_staff and request.user.is_authenticated):
		return redirect('/') 
	leave = get_object_or_404(Leave, id = id)
	Manager_approve = request.user.first_name
	id_lave = id
	#get_object_or_404(Leave, id = id).updated(approve_by =Manager_approve)
	print("id : ",id_lave)
	intermet(id,Manager_approve)
	#Leave.objects.filter(id = id_lave).update(Manger_approve_by = Manager_approve)

	user = leave.user
	user_name = leave.user.first_name
	LinkUser_user_name = leave.name.position

	#x = request.POST[user.first_name]
	#y = x[user.first_name]
	#LinkUser_user_name = request.POST

	getin_user = get_object_or_404(LinkUser, user = user)
	position = getin_user.name.position	
	#Department = getin_user.name.department
	#position_manger = str(position).split(" ")
	#request_user = request.POST[]
	print("user : ",user)
	print("user_name : ",user_name)
	print("LinkUser_user_name : ",LinkUser_user_name)
	print("position : ",position)
	#print("Department : ",Department)
	#print("Department_manger : ",position_manger[0])
	print("Manager_approve : ",Manager_approve)

	x = LinkUser.objects.filter(user = user)
	#employee = Employee.objects.filter(user = user.first_name)
	leave.approve_leave
	# messages.error(request,'Leave successfully approved for {0}'.format(employee),extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('dashboard:userleaveview', id = id)

@login_required(login_url='accounts:login')
def cancel_leaves_list(request):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leaves = Leave.objects.all_cancel_leaves()
	return render(request,'dashboard/leaves_cancel.html',{'leave_list_cancel':leaves,'title':'Cancel leave list'})


@login_required(login_url='accounts:login')
def unapprove_leave(request,id):
	if not (request.user.is_authenticated and request.user.is_superuser):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.unapprove_leave
	return redirect('dashboard:leaveslist') #redirect to unapproved list



@login_required(login_url='accounts:login')
def cancel_leave(request,id):
	if not (request.user.is_superuser or request.user.is_staff and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.leaves_cancel

	messages.success(request,'Leave is canceled',extra_tags = 'alert alert-info alert-dismissible show')
	return redirect('dashboard:leaveslist')#work on redirecting to instance leave - detail view


# Current section -> here
@login_required(login_url='accounts:login')
def uncancel_leave(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.status = 'pending'
	leave.is_approved = False
	leave.save()
	messages.success(request,'Leave is uncanceled,now in pending list',extra_tags = 'alert alert-info alert-dismissible show')
	return redirect('dashboard:canceleaveslist')#work on redirecting to instance leave - detail view


@login_required(login_url='accounts:login')
def leave_rejected_list(request):

	dataset = dict()
	leave = Leave.objects.all_rejected_leaves()

	dataset['leave_list_rejected'] = leave
	return render(request,'dashboard/rejected_leaves_list.html',dataset)


@login_required(login_url='accounts:login')
def reject_leave(request,id):
	dataset = dict()
	leave = get_object_or_404(Leave, id = id)
	leave.reject_leave
	messages.success(request,'Leave is rejected',extra_tags = 'alert alert-info alert-dismissible show')
	return redirect('dashboard:leavesrejected')

	# return HttpResponse(id)

@login_required(login_url='accounts:login')
def unreject_leave(request,id):
	leave = get_object_or_404(Leave, id = id)
	leave.status = 'pending'
	leave.is_approved = False
	leave.save()
	messages.success(request,'Leave is now in pending list ',extra_tags = 'alert alert-info alert-dismissible show')

	return redirect('dashboard:leavesrejected')



#  staffs leaves table user only
@login_required(login_url='accounts:login')
def view_my_leave_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		leaves = Leave.objects.filter(user = user)
		employee = Employee.objects.filter(user = user).first()
		# print(leaves)
		dataset = dict()
		dataset['leave_list'] = leaves
		dataset['employee'] = employee
		dataset['title'] = 'Leaves List'
	else:
		return redirect('accounts:login')
	return render(request,'dashboard/staff_leaves_table.html',dataset)

def intermet(ida,approval):
	Leave.objects.filter(id = ida).update(Manger_approve_by = approval)



