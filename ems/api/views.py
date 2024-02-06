from employee.models import Role,Department,Employee
from employee_information.models import Position,Department_info,Employees_info,Attendace_info
from leave.models import Leave
from .serializers import RoleSerializer,DepartmentSerializer,EmployeeSerializer,PositionSerializer,Department_infoSerializer,Employees_infoSerializer,Attendace_infoSerializer,LeaveSerializer
from rest_framework import viewsets
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


  