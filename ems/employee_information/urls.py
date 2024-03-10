from . import views
#from .views import exportView, exportView2 ,export2
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

app_name = 'employee_information'
urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('home-page', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about-page"),
    path('buildings', views.buildings, name="building-page"),
    path('departments', views.departments, name="department-page"),
    path('manage_building', views.manage_buildings, name="manage_building-page"),
    path('save_building', views.save_building, name="save-building-page"),
    path('delete_building', views.delete_building, name="delete-building"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),
    path('salary', views.employees_salary, name= 'salary-page'),
    path('uplode_csv', views.importExcil, name= 'import'),
    path('attandance',views.TimeshetTest, name = 'attandance'),
    
    path('install_csv',views.file_csv ,name = 'install_csv'), 
    path('salary_csv',views.salary_csv ,name = 'salary_csv'),
    
    path('deduction',views.deduction ,name = 'deduction'), 
    path('salary_increse',views.salary_increse ,name = 'salary_increse'),  



]