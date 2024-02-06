from django.urls import path, include
from api import views 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('role',views.Role,basename='role')
router.register('department',views.Department,basename='department')
router.register('employee',views.Employee,basename='employee')
router.register('position',views.Position,basename='position')
router.register('department_info',views.Department_info,basename='department_info')
router.register('employees_info',views.Employees_info,basename='employees_info')
router.register('attendace_info',views.Attendace_info,basename='attendace_info')
router.register('leave',views.Leave,basename='leave')

urlpatterns = [
    # path('role/', views.RoleList.as_view()),
    # path('department/', views.DepartmentList.as_view()),
    # path('employee/', views.EmployeeList.as_view()),
    # path('position/', views.PositionList.as_view()),
    # path('department_info/', views.Department_infoList.as_view()),
    # path('employees_info/', views.Employees_infoList.as_view()),
    # path('attendace_info/', views.Attendace_infoList.as_view()),
    # path('leave/', views.LeaveList.as_view()),

    # path('Leave/', views.snippet_list),
    # path('Leave/<int:pk>/', views.snippet_detail),

    path('', include(router.urls)),
]