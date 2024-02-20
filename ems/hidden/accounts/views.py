from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import *
from .forms import UserLogin,UserAddForm
from django.contrib.auth.forms import UserCreationForm # create user for dashposrt 
from employee_information.forms import LinkUserForm 
from employee_information.models import  LinkUser



def changepassword(request):
	if not request.user.is_authenticated:
		return redirect('/')
	'''
	Please work on me -> success & error messages & style templates
	'''
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save(commit=True)
			update_session_auth_hash(request,user)

			messages.success(request,'Password changed successfully',extra_tags = 'alert alert-info alert-dismissible show' )
			return redirect('accounts:changepassword')
		else:
			messages.error(request,'Error,changing password',extra_tags = 'alert alert-warning alert-dismissible show' )
			return redirect('accounts:changepassword')
			
	form = PasswordChangeForm(request.user)
	return render(request,'accounts/change_password_form.html',{'form':form})




def register_user_view(request):
	# WORK ON (MESSAGES AND UI) & extend with email field
	if request.method == 'POST': # if tis post then fill this 
		form = UserAddForm(request.POST) 
		#form2 = LinkUserForm(request.POST)
		if form.is_valid(): # if valid 
			"""
			instance = form2.save(commit = False) # before save do this 
			# instance = request.user.id # returen the id of how did this creation 
			
			user = request.POST.get('name')
			assigned_user = User.objects.get(id = user)
			instance.name = assigned_user

			instance.image = request.FILES.get('image')
			
			instance.save() # now save 
			"""
			form.save() # save 
			username = form.cleaned_data.get("username") # get clean like saleh not [saleh]
			password = form.cleaned_data.get("password")# get clean like saleh123 not [saleh123]
			user = authenticate(username = username ,password = password) # get auth by pass user and pass
			login(request , user) # access auth

			#show success message
			messages.success(request,'Account created for {0} !!!'.format(username),extra_tags = 'alert alert-info alert-dismissible show' )
			return redirect('accounts:register')
		else: #if its not valid form 
			messages.error(request,'Username or password is invalid',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('accounts:register')

	# if mehtod is get pass form to fill 
	form = UserAddForm() # in forms.py what you want in to add to form ( email and first name )
	dataset = dict()
	dataset['form'] = form
	dataset['title'] = 'register users'
	return render(request,'accounts/register.html',dataset)




def login_view(request):
	'''
	work on me - needs messages and redirects
	
	'''
	login_user = request.user
	# if he fill up the form  do this if not just pass the form down to fill it 
	if request.method == 'POST':
		form = UserLogin(data = request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			# check username and pass entered 
			user = authenticate(request, username = username, password = password)
			# return true if auth
			if user and user.is_active:
				login(request,user) # pass hem
				if login_user.is_authenticated: # if all okay then redirect to home dashboard or any
					return redirect('dashboard:dashboard')
			else:
				messages.error(request,'Account is invalid',extra_tags = 'alert alert-error alert-dismissible show' )
				return redirect('accounts:login')   
		else: 
			return HttpResponse('data not valid')
	# show this if method get 
	dataset=dict()
	form = UserLogin()

	dataset['form'] = form
	return render(request,'accounts/login.html',dataset)




# def user_profile_view(request):
# 	'''
# 	user profile view -> staffs (No edit) only admin/HR can edit.
# 	'''
# 	user = request.user
# 	if user.is_authenticated:
# 		employee = Employee.objects.filter(user = user).first()
		

# 		dataset = dict()
# 		dataset['employee'] = employee
	
		

# 		return render(request,'dashboard/employee_detail.html',dataset)
# 	return HttpResponse("Sorry , not authenticated for this,admin or whoever you are :)")





def logout_view(request):
	logout(request)
	return redirect('accounts:login')



def users_list(request):
	employees = LinkUser.objects.all()
	return render(request,'accounts/users_table.html',{'employees':employees,'title':'Users List'})


def users_unblock(request,id):
	user = get_object_or_404(User,id = id)
	emp = LinkUser.objects.filter(user = user).first()
	emp.is_blocked = False
	emp.save()
	user.is_active = True
	user.save()

	return redirect('accounts:users')


def users_block(request,id):
	user = get_object_or_404(User,id = id)
	emp = LinkUser.objects.filter(user = user).first()
	emp.is_blocked = True
	emp.save()
	
	user.is_active = False
	user.save()
	
	return redirect('accounts:users')



def users_blocked_list(request):
	blocked_employees = LinkUser.objects.all_blocked_employees()
	return render(request,'accounts/all_deleted_users.html',{'employees':blocked_employees,'title':'blocked users list'})