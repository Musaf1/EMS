from django.http import HttpRequest
from django.shortcuts import redirect

# here take the function called , check if user is authenticated , if its return to home else return to fuction called
def unauthenticated_user(view_func):
    def wrapper_func(request, *ages , **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:dashboard')     
        else:
            return view_func(request, *ages , **kwargs)
    return wrapper_func
