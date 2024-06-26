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
from .attandance import confert_to_sec,inermdite
from .forms import DeductionForm,year_increase
from django.contrib import messages
import time as t
from leave.models import Leave
from xlsxwriter import Workbook

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
@login_required
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')

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

@login_required
def buildings(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    building_list = Building_info.objects.all()
    context = {
        'page_title':'Buildings',
        'buildings':building_list,
    }
    return render(request, 'employee_information/buildings.html',context)

@login_required
def manage_buildings(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    building = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            building = Building_info.objects.filter(id=id).first()
    
    context = {
        'building' : building
    }
    return render(request, 'employee_information/manage_building.html',context)

@login_required
def save_building(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_building = Building_info.objects.filter(id = data['id']).update(name=data['name'], description = data['description'], location = data['location'], status = data['status'])
        else:
            save_building = Building_info(name=data['name'], description = data['description'],  location = data['location'],  status = data['status'])
            save_building.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_building(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    data =  request.POST
    resp = {'status':''}
    try:
        Building_info.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Departments
@login_required
def departments(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    department_list = Department_info.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'employee_information/positions.html',context)
@login_required
def manage_positions(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def employees(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    employee_list = Employees_info.objects.all()
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employee_information/employees.html',context)

@login_required
def manage_employees(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    employee = {}
    departments = Department_info.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    build = Building_info.objects.filter(status = 1).all() 
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
        'positions' : positions,
        'builds' : build
    }
    return render(request, 'employee_information/manage_employee.html',context)

@login_required
def save_employee(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
            buil = Building_info.objects.filter(id=data['build']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees_info.objects.filter(id = data['id']).update(employeeid=data['employeeid'], name=data['name'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'], build= buil,department = dept,position = pos,startdate = data['startdate'],salary = data['salary'], acount_number = data['acount_number'], Nationality = data['Nationality'])
            else:
                save_employee = Employees_info(employeeid=data['employeeid'], name=data['name'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'], build= buil,department = dept,position = pos,startdate = data['startdate'],salary = data['salary'] , acount_number = data['acount_number'],status = data['status'], Nationality = data['Nationality'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"employeeid":data['employeeid'], "name" : data['name'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department" : data['department'],"position" : data['position'],"startdate" : data['startdate'],"salary" : data['salary'],"acount_number" : data['acount_number'], "status" : data['status'], "Nationality" :data['Nationality'],}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
@login_required
def employees_salary(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    employee_list = Employees_info.objects.all()
    '''
    deduction = employee_list
        
    for i in range(len(deduction)):
        salary = deduction[i].salary
        if employee_list[i].Nationality == 'Saudi':
            reuslt = salary*0.11
        else:
            reuslt = salary*0.025
        total = salary - reuslt
        #deduction[i].deduction = reuslt
        Employees_info.objects.filter(employeeid=deduction[i].employeeid).update(gosi =reuslt, total_salary =total)
        
    pirodOB = pirod.objects.all()
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


@login_required
def importExcil(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
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

@login_required
def Timeshet(request): 
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    m1 = Employees_info.objects.all()
    with open ('employee_information/Attandance.csv','w') as f :
        f.write(f'"name","time attendace","time leaves" , "total working hours"')
        for i in m1:
            if date(2023,8,21)<i.date  and i.date <date(2023,8,25):
                f.write(f'\n{i.name},{i.date} ,{i.Time_attendace} , {i.time_leaves}')

@login_required
def TimeshetTest(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    employee_list = Employees_info.objects.all()
    deduction = employee_list
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    if request.POST :
        try:
            form = attendaceForm(request.POST)
            # if form okay save in DB
            print("name_id : ", request.POST["Employee"])
            print("Start date : ", request.POST["start_perod"])
            print("end date : ", request.POST["end_perod"])
            if request.POST["start_perod"] > request.POST["end_perod"]:
                return render(request, 'employee_information/attandance.html',context)

    
            if form.is_valid():
                print("is valid")
                form.save()
                print("saved")

                employee_name =form.cleaned_data['Employee']
                start_pirod =form.cleaned_data['start_perod']
                end_pirod =form.cleaned_data['end_perod']
                attendace_list = Attendace_info.objects.filter(name = employee_name )

            else:
                print("Form not valid")  

                
            context = {
                'page_title':'Employees',
                'employees':employee_list,
                'start_pirod' : start_pirod,
                'end_pirod' :end_pirod,
                'form': form,
                'attendace_list': attendace_list,
            }
        except:
            print(" except active")
            return render(request, 'employee_information/attandance.html',context)
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

@login_required
def file_csv(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = "attachment; filename= attendace.csv"
    pirodOB = Pirod.objects.all()
    start_pirod =pirodOB[len(pirodOB)-1].start_perod
    end_pirod =pirodOB[len(pirodOB)-1].end_perod
    print("installing atendace CSV from " + str(start_pirod) + " to " + str(end_pirod))
    workbook = Workbook(response)
    data = Attendace_info.objects.filter(date__range=[start_pirod, end_pirod])
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True, 'bg_color': 'yellow'})
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 10)
    worksheet.write(0, 0, 'Name')
    worksheet.write(0, 1, 'Date')
    worksheet.write(0, 2, 'Time Attendace')
    worksheet.write(0, 3, 'Time Leaves')
    worksheet.write(0, 4, 'Total Time')
    i=1
    for row in data:
            if row.total_time < 8:  # Replace `condition` with your actual logic
                worksheet.write(i, 0, str(row.name), bold)
                worksheet.write(i, 1, str(row.date), bold)
                worksheet.write(i, 2, str(row.Time_attendace), bold)
                worksheet.write(i, 3, str(row.time_leaves), bold)
                worksheet.write(i, 4, str(row.total_time), bold)
                i+=1
            else:
                worksheet.write(i, 0, str(row.name))
                worksheet.write(i, 1, str(row.date))
                worksheet.write(i, 2, str(row.Time_attendace))
                worksheet.write(i, 3, str(row.time_leaves))
                worksheet.write(i, 4, str(row.total_time))
                i+=1        
    workbook.close()
    return response

@login_required
def salary_csv(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = "attachment; filename= Salary.csv"
    pirodDB = Pirod.objects.last()
    start_date =  pirodDB.start_perod
    end_date = pirodDB.end_perod
    print("######################### pirod.start_pirod : ", pirodDB.start_perod)
    print("######################### pirod.start_pirod : ", pirodDB.end_perod)

    #Get the number of days in the current month using calendar and datetime modules
    now = datetime.datetime.now()
    print("$$$$$$$$$$$$$$$$$$$$$ now: $$$$$$$$$$$$$$$$$$$$$", now)
    month = pirodDB.start_perod.month
    year = now.year
    num_days = calendar.monthrange(year, month)[1]
    print(f"Number of days in {calendar.month_name[month]} {year}: {num_days}")
    print("************************start_pirod : {0} , end_pirod{1} *********** :".format(start_date, end_date))
    x = str(end_date - start_date)
    print("************************ end_pirod - start_pirod: *********** :",x)
    split = x.split(" ")
    y = int(split[0])
    temp = y + 1   # number of days search by user in our site 
    print("***************************** number of days : *********** :", temp  )
    data = Attendace_info.objects.filter( date__range = [start_date, end_date]) 

    employee_list = Employees_info.objects.all()
    leaves = Leave.objects.all()
    absent = 0
    # pirodOB = Attendace_info.objects.filter(date__range=[start_pirod, end_pirod])
    
    for i in range(len(employee_list)):
        print("--------------------- im in salary_csv start first loop : {0} ---------------------- ".format(employee_list[i].name))
        approved_leave_days = 0
        for L in range(len(leaves)): 
            states = 'pending'
            if  leaves[L].user_id == employee_list[i].id :
                states = leaves[L].status 
            if states == 'approveed' and leaves[L].leavetype != 'task':
                days_approvied = leaves[L].leave_days
                approved_leave_days += int(days_approvied)
                
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
        if employee_list[i].Nationality == 'Saudi':
            gosi = salary*0.11
        else:
            gosi = salary*0.025
        counter1 = 0
        counter2 = 0
        counter3 = 0 
        counter4 = 0
        counter5 = 0 
        detaction = 0

        day_salary = reuslt/num_days 
        hour_salary = day_salary/8
        absent_days = 0
        num_of_days_attended = 0
        for j in range(len(data)): 
            print("------------------ salary_csv second loop --------------------") 
            if  data[j].name_id == employee_list[i].id :
                print("------------------ salary_csv started second loop total salry : {0} day salary {1} --------------- ".format(reuslt ,day_salary))
                #if employee_list[i].name == pirodOB[j].name:
                start_pirod =data[j].Time_attendace
                end_pirod =data[j].time_leaves
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
                
                #print("--------------- second loop : total detaction = {0} ------------------- ".format(detaction))

            print("--------------- im in salary_csv second loop : total detaction = {0} ------------- ".format(detaction))
        print("---------------  salary_csv second loop  ended succsufly---------------------- ")

        num_of_days_attended = Attendace_info.objects.filter( date__range = [start_date, end_date], name_id = employee_list[i].id).count()
        print("||||||||||||||||||||||||||||||||||| name |||||||||||||| :" , employee_list[i].id)
        print("||||||||||||||||||||||||||||||||||| number of days attedned |||||||||||||| :" , num_of_days_attended)
        if num_of_days_attended < temp : 
            absent_days =  (temp - num_of_days_attended) + approved_leave_days 

        print('///////////// absent_days : {0} //////////////////'.format(absent_days))
        if absent_days > 0:
            if absent_days == 1 :
                detaction += day_salary*2
            elif absent_days == 2 :
                detaction += day_salary*4
            elif absent_days == 3 :
                detaction += day_salary*6
            elif absent_days == 2 :
                detaction += day_salary*8
            print("--------------------------- detaction abesent : {0}----------------".format(detaction))


        #deduction[i].deduction = reuslt
        # update the salary after gosi detaction and other detaciton 
        print("--------------------------  updating DB -------------------------------")
        temp2 = day_salary*num_of_days_attended
        print("*****************************salary*********** :", temp2  )
        print("*****************************detaction*********** :", detaction  )
        print("*****************************gosi*********** :", gosi  )

        total = round(temp2 - detaction ,2)       
        print("*****************************total salary*********** :", total  )
        Employees_info.objects.filter(employeeid=employee_list[i].employeeid).update(gosi = gosi,deduction =detaction ,total_salary =total )
        print("-------------------------- DB updated succsufly -------------------------------")

    print("-------------------------- first loob ended succsufly -------------------------------")

    print("----------------- installing csv function--------------- ")
    info = Employees_info.objects.all()
    # create a csv 
    writer = csv.writer(response)
    # add columns to csv
    writer.writerow(['From', start_date, 'To',end_date])
    writer.writerow([''])

    writer.writerow(['Name', 'Salary', 'Gosi', 'Detaction', 'Basic','Home', 'Transportation', 'OtherPayment','Other Deduction', 'Total_salary', 'acount_number'])
    # loop over and add the data 
    for i in info : 
        writer.writerow([i.name, i.salary, i.gosi, i.deduction +  i.other_deduction  , i.total_salary*0.65, i.total_salary*0.25, i.total_salary*0.10,i.other_payment, i.other_deduction, i.total_salary - i.other_deduction + i.other_payment, i.acount_number])
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

@login_required
def deduction(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    form = DeductionForm(request.POST)
    if request.method =='POST':
        print("-----------mtheod is post and requst.name :")
        
        if form.is_valid():
            print("form is valid: ")
            form.save()  
            employee =form.cleaned_data['name']
            inermdite(employee)
            messages.success(request, 'Add deduction successfully' )
    return render(request, 'employee_information/deduction.html',{'form':form})

@login_required
def deduction(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    form = DeductionForm(request.POST)
    if request.method =='POST':
        print("-----------mtheod is post and requst.name :")
        
        if form.is_valid():
            print("form is valid: ")
            form.save()  
            employee =form.cleaned_data['name']
            inermdite(employee)
            messages.success(request, 'Add deduction successfully' )
    return render(request, 'employee_information/deduction.html',{'form':form})

"""    user = form.cleaned_data.get("username")
        print("request.employee_id : ", form.employee_id)
        print("request.other_deduction : ", request.other_deduction)
        Employees.objects.filter(employeeid=request.employee_id).update(other_deduction =request.other_deduction)
        

        
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
   
        """


# this function add increase to salary by % 
# EX:  take 10 and convert it to 0.10
# get the salary form database
# update the salary by adding 10% to it 
@login_required
def salary_increse(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect('accounts:login')
    form = year_increase(request.POST)
    
    if request.method =='POST':
        print("-----------mtheod is post and requst.name :")
        if form.is_valid():
            print("form is valid ")            
            employee =form.cleaned_data['name']
            input_year_increase =form.cleaned_data['year_increase']
            Employee = Employees_info.objects.filter(name = employee )[0]
            temp = (input_year_increase/100) + 1

            """
            remove to debug 
            print("-------Employee : ", Employee.salary)
            print("-------name : ", employee)
            print("-------input_year_increase : ", input_year_increase)
            print("-------temp : ", temp)
            """

            Employees_info.objects.filter(name=employee).update( salary= Employee.salary*temp)
            
            messages.success(request, 'increase added successfly' )
    return render(request, 'employee_information/year_increase.html',{'form':form})

"""
Delelte me 

def welcome(request):
	return render(request,'accounts/tow_systems_entery.html')
"""
