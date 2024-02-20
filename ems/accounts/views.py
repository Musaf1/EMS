from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import *
from .forms import UserLogin,UserAddForm , CreationUserForm, User_Update_Profile,SignUpForm,ProfilePicForm
from .decorators import unauthenticated_user
from employee_information.forms import LinkUserForm
from .models import Profile
from django import forms




def registerpage(request):
    form = CreationUserForm()
    # cheack if method is post and user name not used before then create user 
    if request.method == 'POST' :
        form = CreationUserForm(request.POST)
        # if form valid then save it and show a success form in the templet 
        if form.is_valid():
            form.save()  
            user = form.cleaned_data.get("username")
            messages.success(request, ' Account has successfly created for : ' + user)
            return redirect('accounts:login')
    context = {'form': form}
    return render (request,'accounts/register.html',context)

def loginpage(request):
    
    # if method is post get the username and pass form the form 
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')
        # check user is in our DB  then return user to home page 
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')     
        else :
            messages.info(request, 'Username or Password incorrect')

    context = {}
    return render (request,'accounts/login.html')



def logout_view(request):
	logout(request)
	return redirect('accounts:login')


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

def users_list(request):
	employees = Employee.objects.all()
	return render(request,'accounts/users_table.html',{'employees':employees,'title':'Users List'})

"""
def users_list(request):
	employees = Employee.objects.all()
	return render(request,'accounts/users_table.html',{'employees':employees,'title':'Users List'})
"""

def users_unblock(request,id):
	user = get_object_or_404(User,id = id)
	emp = Employee.objects.filter(user = user).first()
	emp.is_blocked = False
	emp.save()
	user.is_active = True
	user.save()

	return redirect('accounts:users')


def users_block(request,id):
	user = get_object_or_404(User,id = id)
	emp = Employee.objects.filter(user = user).first()
	emp.is_blocked = True
	emp.save()
	
	user.is_active = False
	user.save()
	
	return redirect('accounts:users')



def users_blocked_list(request):
	blocked_employees = Employee.objects.all_blocked_employees()
	return render(request,'accounts/all_deleted_users.html',{'employees':blocked_employees,'title':'blocked users list'})
    

def Update_Profile(request):
	user = request.user
	form = User_Update_Profile(instance= user)
	if request.method == 'POST':
		form = User_Update_Profile(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user.id
			print("user : ",user)
			assigned_user = User.objects.get(id = user)
			print("assigned_user : ",assigned_user)
			print("request.POST.name : ",request.POST.get('username'))
			instance.first_name = request.POST.get('username')

			#instance.image = request.FILES.get('image')

			#instance.save()
			

			return  redirect('dashboard:employees')
		else:
			messages.error(request,'Trying to create dublicate employees with a single user account ',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('dashboard:employeecreate')
	dataset = dict()
	form = User_Update_Profile()
	dataset['form'] = form
	dataset['title'] = 'register employee'
	return render(request,'dashboard/employee_create.html',dataset)
	
		
'''
	

		form = User_Update_Profile(request.POST , request.FILES ,instance= user)
		if form.is_valid():
			form.save()

	context = {'form':form}
#	form = Update_Profile(request.user)
	return render(request,'accounts/Profile.html',context)
#	return render(request,'accounts/Profile.html',{'employees':blocked_employees,'title':'blocked users list'})

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
'''

def profile_list(request):
	if request.user.is_authenticated:
		profiles = Profile.objects.all()
		return render(request, "accounts/profile_list.html",{"profiles":profiles})
	else :
		messages.error(request,'you must be login ',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('accounts:login')
# This method return your followrs and who you follow to  
def profile(request,pk):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user_id=pk)	
		return render(request,"accounts/profile2.html", {"profile":profile})
	else :
		messages.error(request,'you must be login ',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('accounts:login')
	
def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, ' Account has successfly created for : ' + username)
			return redirect('dashboard:dashboard')
	context = {'form': form}
	return render (request,'accounts/register2.html',context)

	
def update_uesr(request):
	if request.user.is_authenticated:
		# get data id and info of user the loged in now
		current_user = User.objects.get(id = request.user.id)
		user_form = CreationUserForm(request.POST or None, request.FILES or None, instance = current_user)

		# get the profile of the same user
		profile_user = Profile.objects.get(user__id =  request.user.id )
		profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance = profile_user)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()			
			login(request,current_user)
			messages.success(request,'Your profile has been updated!',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('dashboard:dashboard') # dashboard/welcome/
		return render(request,'accounts/update_uesr.html',{'user_form': user_form, 'profile_form':profile_form})

#			
	else: 
		messages.error(request,'you must be login ',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('accounts:login')