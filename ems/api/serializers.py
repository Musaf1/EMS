from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from employee.models import *
from employee_information.models import *
from leave.models import Leave

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', "email", "mac", "change_mac")
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role
    fields = '__all__' 

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = '__all__'  

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'

class Building_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Building_info
    fields = '__all__'      

class Department_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department_info
    fields = '__all__'      

class Employees_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employees_info
    fields = '__all__'

class Attendace_infoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attendace_info
    fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Leave
    fields = '__all__'

class LinkUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = LinkUser
    fields = '__all__'
  
class PirodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pirod
    fields = '__all__'                    

    