from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department_info, Position, Employees_info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
from .models import *
from .forms import employeesForm, attendaceForm,formFormat
from tablib import Dataset
from .resource import PersonResources
from datetime import date
from datetime import time 
import datetime
from django.views.generic import ListView,FormView,TemplateView
from .admin import exportForm
import pandas as pd 
import chardet
import csv
import calendar 
from .attandance import confert_to_sec
employees = [

    {
        'employeeid':1,
        'name':"John D Smith",
        'contact':'09123456789',
        'address':'Sample Address only'
    },{
        'employeeid':2,
        'name':"Claire C Blake",
        'contact':'09456123789',
        'address':'Sample Address2 only'
    }

]
# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department_info.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees_info.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Departments
@login_required
def departments(request):
    department_list = Department_info.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department_info.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)

@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department_info.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_department = Department_info(name=data['name'], description = data['description'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department_info.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Positions
@login_required
def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'employee_information/positions.html',context)
@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
# Employees
def employees(request):
    employee_list = Employees_info.objects.all()
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employee_information/employees.html',context)
@login_required
def manage_employees(request):
    employee = {}
    departments = Department_info.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees_info.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/manage_employee.html',context)

@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employees_info.objects.exclude(id = data['id']).filter(employeeid = data['employeeid'])
    else:
        check  = Employees_info.objects.filter(employeeid = data['employeeid'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department_info.objects.filter(id=data['department']).first()
            pos = Position.objects.filter(id=data['position']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees_info.objects.filter(id = data['id']).update(employeeid=data['employeeid'], name=data['name'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department = dept,position = pos,startdate = data['startdate'],salary = data['salary'], acount_number = data['acount_number'], status = data['status'])
            else:
                save_employee = Employees_info(employeeid=data['employeeid'], name=data['name'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department = dept,position = pos,startdate = data['startdate'],salary = data['salary'] , acount_number = data['acount_number'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"employeeid":data['employeeid'], "name" : data['name'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department" : data['department'],"position" : data['position'],"startdate" : data['startdate'],"salary" : data['salary'],"acount_number" : data['acount_number'], "status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees_info.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    departments = Department_info.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees_info.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)



# Employees
def employees_salary(request):
    employee_list = Employees_info.objects.all()
    deduction = employee_list
        
    for i in range(len(deduction)):
        salary = deduction[i].salary
        reuslt = salary*0.11
        total = salary - reuslt
        #deduction[i].deduction = reuslt
        Employees_info.objects.filter(employeeid=deduction[i].employeeid).update(gosi =reuslt, total_salary =total)
        
    '''pirodOB = pirod.objects.all()
    start_pirod =pirodOB[len(pirodOB)-1].start_perod
    end_pirod =pirodOB[len(pirodOB)-1].end_perod
    '''    
    # get data form database
    #data = attendace.objects.filter(date__range=[start_pirod, end_pirod])
    
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employee_information/salary.html',context)



def importExcil(request):
    if request.method =='POST':
        peronl = PersonResources()
        dataset= Dataset()
        new_per = request.FILES['my_file']
        imported_data = dataset.load(new_per.read(),format='xlsx')
        for data in imported_data:
            value = Employees_info(
                data[1],
                data[2],
                
            )
            value.save()
    return render(request ,'employee_information/uplode_attentace.html')
    
@login_required
def salary(request):
    employee = {}
    departments = Department_info.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees_info.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)

def Timeshet(request): 
    m1 = Employees_info.objects.all()
    with open ('employee_information/Attandance.csv','w') as f :
        f.write(f'"name","time attendace","time leaves" , "total working hours"')
        for i in m1:
            if date(2023,8,21)<i.date  and i.date <date(2023,8,25):
                f.write(f'\n{i.name},{i.date} ,{i.Time_attendace} , {i.time_leaves}')
def TimeshetTest(request):
    employee_list = Attendace_info.objects.all()
    deduction = employee_list
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    if request.POST :
        form = attendaceForm(request.POST,request.FILES)
        # to use the value enter without save in DB
        print("im in TimeshetTest request.POST") 
        # if form okay save in DB
        if form.is_valid():
        #    print("is valid")
            form.save()
        pirodOB = Pirod.objects.all()
        start_pirod =pirodOB[len(pirodOB)-1].start_perod
        end_pirod =pirodOB[len(pirodOB)-1].end_perod
        #change_type = request.POST["start_perod"]
        #change_type = (date) change_type
        print(type(request.POST["start_perod"]))
        print(request.POST["start_perod"])
        print(request.POST["end_perod"])

        context = {
            'page_title':'Employees',
            'employees':employee_list,
            'start_pirod' : start_pirod,
            'end_pirod' : end_pirod,
        }
    return render(request, 'employee_information/attandance.html',context)
'''
def test(request): 
    if request.POST:   
        #form = attendaceForm(request.POST,request.FILES)
        print("test")
        # to use the value enter without save in DB
        print(request.POST["end_perod"]) 
        # if form okay save in DB
        #if form.is_valid():
        #    print("is valid")
        #    form.save()
        #Z    return redirect(home)
    return render(request, 'employee_information/test_input.html',{'form':attendaceForm})

# export excl , model in DB , form_class maked in forms 
class exportView(ListView,FormView):
    model = attendace
    template_name = 'test_new_input.html'
    form_class = formFormat
    

    def post(self,requst,**kwargs):
        qs = self.get_queryset() # add filters
        Dataset = exportForm().export(qs)

        # get use chose post  (format user chose)
        format = requst.POST.get(format)
        if format == 'xls':
            ds = Dataset.xls
        elif format == 'csv': 
            ds =Dataset.csv
        else:
            ds = Dataset.json

        # return httpresponse 
        response = HttpResponse(ds,content_type = f"{format}") # return the file 
        response['Content-Disposition'] = f"attachment; filename=posts.{format}"
        return response
    
class exportView2(TemplateView):
    template_name = 'test_new_input.html'

def export2(requst,format):
    employee_list = exportForm()
    print(employee_list)

    post_recource = employee_list
    dataset = post_recource.export()
    if format[5:-1] == 'csv':
        dataset_format = dataset.csv
        file = csv.reader(dataset_format)
        """ print(type(file))
        for row in file:
            print(row)
        """
        #df = pd.read_csv(csv(dataset_format))
        #print(df)
        """header = []
        header = file.readlines()
        print(header)"""
        """rows = []
        for row in file:
            rows.append(row)
        print(rows)"""
        print("--------------------im in csv--------------------- ") 
        #print(dataset_format[name])           

    else:
        dataset_format = dataset.xls 
        """ with open (dataset_format,'r' ,encoding='Windows-1252') as f :
            print("isit ?")            
            result = chardet.detect(dataset_format)
            print("encode : " ,result)
            #df = pd.read_csv(dataset_format, encoding='Windows-1252')
            #print(f.read())"""
        """ df = pd.read_csv(dataset_format, encoding='ISO-8859-1') 
        print(df)"""
        print("-------------------im in xls----------------------" )
    response = HttpResponse(dataset_format,content_type = "text/{format[5:-1]}")
    response['Content-Disposition'] = f"attachment; filename= posts.{format[5:-1]}"
    return response
'''

def file_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = "attachment; filename= attendace.csv"

    pirodOB = Pirod.objects.all()
    start_pirod =pirodOB[len(pirodOB)-1].start_perod
    end_pirod =pirodOB[len(pirodOB)-1].end_perod
    
    print("installing atendace CSV from " + str(start_pirod) + " to " + str(end_pirod))

    # create a csv 
    writer = csv.writer(response)
    # get data form database
    data = Attendace_info.objects.filter(date__range=[start_pirod, end_pirod])
    # add columns to csv
    writer.writerow(['name', 'date', 'Time_attendace', 'time_leaves', 'total_time'])
    print("-----------------im in file_csv function--------------- ")
    # loop over and add the data 
    for i in data : 
        writer.writerow([i.name, i.date, i.Time_attendace, i.time_leaves, i.total_time])

    return response

def salary_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = "attachment; filename= Salary.csv"
    pirodOB = Pirod.objects.all()
    start_pirod =pirodOB[len(pirodOB)-1].start_perod
    end_pirod =pirodOB[len(pirodOB)-1].end_perod

    #Get the number of days in the current month using calendar and datetime modules
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    num_days = calendar.monthrange(year, month)[1]
    print(f"Number of days in {calendar.month_name[month]} {year}: {num_days}")
    data = Attendace_info.objects.filter( date__range = [start_pirod, end_pirod]) 

    employee_list = Employees_info.objects.all()
    pirodOB = Attendace_info.objects.filter(date__range=[start_pirod, end_pirod])
    
    for i in range(len(employee_list)):
        print("--------------------- im in salary_csv start first loop : {0} ---------------------- ".format(employee_list[i].name))
        
        # Get the employee attendace
        """
        try:
        except:
            print("--------------------- exception enterted -------------------")
            continue
        """
        #if  data[i].name == employee_list[i].id :

        salary = employee_list[i].salary
        reuslt = salary*0.89
        gosi = salary*0.11
        counter1 = 0
        counter2 = 0
        counter3 = 0 
        counter4 = 0
        counter5 = 0 
        detaction = 0

        for j in range(len(data)-1): 
            if  data[j].name_id == employee_list[i].id :
                day_salary = reuslt/num_days 
                hour_salary = day_salary/8
                print("------------------ salary_csv start second loop total salry : {0} day salary {1} --------------- ".format(reuslt ,day_salary))
                #if employee_list[i].name == pirodOB[j].name:
                start_pirod =data[j].Time_attendace
                end_pirod =data[j].time_leaves
                absent_days = data[j].absent_days
                if time(8,30,0) >= start_pirod > time(8,15,0): 
                    counter1 += 1
                    print("deleaed up to 15 m ")
                    if counter1 == 2 : 
                        detaction += day_salary *0.05
                    elif counter1 == 3:
                        detaction += day_salary *0.10
                    elif counter1 > 3:
                        detaction += day_salary *0.20
                # delay up to 30 m
                elif time(9,0,0) >= start_pirod > time(8,30,0): 
                    counter2 += 1
                    print("deleaed  30 to 60 m ")
                    if counter2 == 1 : 
                        detaction += day_salary *0.25
                    elif counter2 == 2 :
                        detaction += day_salary *0.50
                    elif counter2 == 3 :
                        detaction += day_salary *0.75
                    elif counter2 > 3 :
                        detaction += day_salary 
                # delay more than 1 hour
                elif start_pirod > time(9,0,0): 
                    counter3 +=1
                    print("deleaed more than 1 hour m ")
                    daly_hours = confert_to_sec(start_pirod) - confert_to_sec(time(8,0,0))  
                    if counter3 == 1:
                        detaction += hour_salary * daly_hours
                    elif counter3 == 2 :
                        detaction += (hour_salary * daly_hours) + day_salary  
                    elif counter3 == 3 :
                        detaction += (hour_salary * daly_hours) + (day_salary*2)   
                    elif counter3 > 3 :
                        detaction += (hour_salary * daly_hours) + (day_salary*3)       
            
                # calc the early leave 
                if time(15,45,0) <= end_pirod < time(16,0,0): 
                    counter4 += 1
                    print("leave befor 15 m end of work ")
                    leave_hours = confert_to_sec(time(16,0,0)) - confert_to_sec(end_pirod )  
                    if counter4 == 1:
                        detaction += hour_salary * leave_hours
                    elif counter4 == 2 :
                        detaction += (hour_salary * leave_hours) + (day_salary  * 0.10)
                    elif counter4 == 3 :    
                        detaction += (hour_salary * leave_hours) + (day_salary  * 0.25)
                    elif counter4 > 3 :    
                        detaction += (hour_salary * leave_hours) + day_salary 
                if end_pirod < time(15,45,0): 
                    counter5 += 1
                    leave_hours = confert_to_sec(time(16,0,0)) - confert_to_sec(end_pirod )  
                    print("leave befor more than 15 m end of work ")
                    if counter5 == 1:
                        detaction += (hour_salary * leave_hours) + (day_salary  * 0.10)
                    elif counter5 == 2 :
                        detaction += (hour_salary * leave_hours) + (day_salary  * 0.25)
                    elif counter5 == 3 :    
                        detaction += (hour_salary * leave_hours) + (day_salary  * 0.5)
                    elif counter5 > 3 :    
                        detaction += (hour_salary * leave_hours) + day_salary 
                print("--------------------------- dalay detactoin : {0}----------------".format(detaction))

                if absent_days != 0:
                    if absent_days == 1 :
                        detaction += day_salary*2
                    elif absent_days == 2 :
                        detaction += day_salary*4
                    elif absent_days == 3 :
                        detaction += day_salary*6
                    elif absent_days == 2 :
                        detaction += day_salary*8
                    print("--------------------------- detaction abesent : {0}----------------".format(detaction))
                
                #print("--------------- second loop : total detaction = {0} ------------------- ".format(detaction))

            print("--------------- im in salary_csv second loop : total detaction = {0} ------------- ".format(detaction))
        print("---------------  salary_csv second loop  ended succsufly---------------------- ")



        #deduction[i].deduction = reuslt
        # update the salary after gosi detaction and other detaciton 
        print("--------------------------  updating DB -------------------------------")
        total = round(salary - detaction - gosi,2)
        Employees_info.objects.filter(employeeid=employee_list[i].employeeid).update(gosi = gosi,deduction =detaction ,total_salary =total )
        print("-------------------------- DB updated succsufly -------------------------------")

    print("-------------------------- first loob ended succsufly -------------------------------")

    print("----------------- installing csv function--------------- ")
    # create a csv 
    writer = csv.writer(response)
    # add columns to csv
    writer.writerow(['name', 'Total_salary', 'gosi', 'detaction', 'payed_salary'])
    # loop over and add the data 
    for i in employee_list : 
        writer.writerow([i.name, i.salary, i.gosi, i.deduction, i.total_salary])
    print("----------------- csv installed function--------------- ")

    return response

""" 
     # decleration
    pirodOB = pirod.objects.all()
    name2 = employee_list[len(employee_list)-1].name
    name =pirodOB[len(pirodOB)-1].name
    
    print("--------------------  calc" + str(start_pirod) + " to " + str(end_pirod))
    # calcluate the morning delay detaction
    


    print("name form deduction : ", name2)
    print("name form attendace : ", name)

"""