from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from employee.models import Role,Department,Employee
from employee_information.models import Position,Department_info,Employees_info,Attendace_info,LinkUser,Pirod,Shift
from leave.models import Leave

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role
    fields = ['id', 'name', 'description', 'created', 'updated']

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ['id', 'name', 'description', 'created', 'updated']   

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ['id', 'user', 'image', 'firstname', 'lastname', 'othername', 'birthday', 'department', 'role', 'startdate', 'employeetype', 'employeeid', 'dateissued', 'is_blocked', 'is_deleted', 'created', 'updated']    

class PositionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = ['id', 'name', 'description', 'created', 'updated']

class Department_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department_info
    fields = ['id', 'name', 'description', 'location', 'created', 'updated']      

class Employees_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employees_info
    fields = ['id', 'employeeid','name','gender','dob','contact','address','email','department','position','shift','startdate','salary','gosi','deduction','total_salary','not_paid_hours','acount_number','status','created','updated','employeetype']    

class Attendace_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attendace_info
    fields = ['id', 'name','date','Time_attendace','time_leaves','total_time','absent_days']

class LeaveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Leave
    fields = ['id', 'user','startdate','enddate','leavetype','reason','defaultdays','status','is_approved','updated','created']  

class LinkUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = LinkUser
    fields = ['id', 'user','name','image','is_blocked','is_deleted','dateissued']  

class PirodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pirod
    fields = ['id', 'start_perod','end_perod']   

class ShiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shift
    fields = ['id','name', 'start','end']                    

    