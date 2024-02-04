from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import *
from .forms import UserLogin,UserAddForm , CreationUserForm
from .decorators import unauthenticated_user




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

			messages.success(request,'Password changed successfully',extra_tags = 'alert alert-success alert-dismissible show' )
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
    
