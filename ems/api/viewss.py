from employee.models import Role,Department,Employee
from employee_information.models import Position,Department_info,Employees_info,Attendace_info,LinkUser,Pirod,Shift
from leave.models import Leave
from .serializers import UserSerializer,RoleSerializer,DepartmentSerializer,EmployeeSerializer,PositionSerializer,Department_infoSerializer,Employees_infoSerializer,Attendace_infoSerializer,LeaveSerializer,LinkUserSerializer,PirodSerializer,ShiftSerializer
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.utils import timezone,dateformat
from django.http import JsonResponse
# Create your views here.

class Role(viewsets.ModelViewSet):
  queryset = Role.objects.all()
  serializer_class = RoleSerializer  

class Department(viewsets.ModelViewSet):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer  

class Employee(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer  

class Position(viewsets.ModelViewSet):
  queryset = Position.objects.all()
  serializer_class = PositionSerializer  

class Department_info(viewsets.ModelViewSet):
  queryset = Department_info.objects.all()
  serializer_class = Department_infoSerializer  

class Employees_info(viewsets.ModelViewSet):
  queryset = Employees_info.objects.all()
  serializer_class = Employees_infoSerializer  

class Attendace_info(viewsets.ModelViewSet):
  queryset = Attendace_info.objects.all()
  serializer_class = Attendace_infoSerializer  

class Leave(viewsets.ModelViewSet):
  queryset = Leave.objects.all()
  serializer_class = LeaveSerializer 

class Pirod(viewsets.ModelViewSet):
  queryset = Pirod.objects.all()
  serializer_class = PirodSerializer

class Shift(viewsets.ModelViewSet):
  queryset = Shift.objects.all()
  serializer_class = ShiftSerializer 

class LinkUser(viewsets.ModelViewSet):
  queryset = LinkUser.objects.all()
  serializer_class = LinkUserSerializer     

def ServerTime(request):
    d =dateformat.format(timezone.localtime(timezone.now()),'H:i')
    return JsonResponse({'time': d})

def ServerDate(request):
    d =timezone.localtime(timezone.now()).timestamp()
    return JsonResponse({'date': d})

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )   


# class LeaveList(ListAPIView):
#   queryset = Leave.objects.all()
#   serializer_class = LeaveSerializer  

# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Leave.objects.all()
#         serializer = LeaveSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = LeaveSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Leave.objects.get(pk=pk)
#     except Leave.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = LeaveSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = LeaveSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 


  