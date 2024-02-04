from datetime import date 
from employee_information.models import attendace
from employee_information.models import Employees


# take info from database
# m1 = Employees.objects.all()
# m1[0].Time_attendace

# covert time to seconds 
def confert_to_sec(time):
    time = str(time) 
    time = time.split(":") 
    # print("im in" ,time.split(":")) 
    #print("{0}  {1}  {2}".format(time[0],time[1],time[2])) 
    total1 = int(time[0]) * 60 * 60
    total1 += int(time[1]) * 60 
    total1 += int(time[2]) 
    hour = round(total1 /60/60 ,2) 
    return   hour
"""
#d = confert_to_sec(m1[0].Time_attendace)
#d2 = confert_to_sec(m1[0].time_leaves)
# find total time worked 
#total = d2 - d

# write data from Database to csv file 
# Note :  search form  start date (2023,8,21) , end date = date(2023,8,25) 
with open ('employee_information/Attandance.csv','w') as f :
    f.write(f'"name","time attendace","time leaves" , "total working hours"')
    for i in m1:
        if date(2023,8,21)<i.date  and i.date <date(2023,8,25):
            f.write(f'\n{i.name},{i.date} ,{i.Time_attendace} , {i.time_leaves}')

# total = (confert_to_sec(i.time_leaves) - confert_to_sec(i.Time_attendace)) / 60/60

# conder to hoour.min
def confert_to_hour(time):
    hour = round(time /60/60 ,2) 
    return   hour
'''

m1 = attendace.objects.create(name='move1', date=date(2023,8,21) , Time_attendace)





 name = models.TextField()
    date = models.DateField(_('Date attended'),help_text='date staff Date attended',blank=False,null=True)
    Time_attendace = models.TimeField(_('Date attended'),help_text='date staff Date attended')
    time_leaves = models.TimeField(_('Date attended'),help_text='date staff Date attended')'''
    
                              
                            





"""