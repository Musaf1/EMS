from django.urls import path, include
from api import viewss 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router=DefaultRouter()
router.register('role',viewss.Role,basename='role')
router.register('department',viewss.Department,basename='department')
router.register('employee',viewss.Employee,basename='employee')
router.register('position',viewss.Position,basename='position')
router.register('department_info',viewss.Department_info,basename='department_info')
router.register('employees_info',viewss.Employees_info,basename='employees_info')
router.register('attendace_info',viewss.Attendace_info,basename='attendace_info')
router.register('building_info',viewss.Building_info,basename='building_info')
router.register('leave',viewss.Leave,basename='leave')
router.register('linkUser',viewss.LinkUser,basename='linkUser')
router.register('pirod',viewss.Pirod,basename='pirod')

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
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('user/', viewss.UserRecordView.as_view(), name='users'),
    path('time/', viewss.ServerTime, name='time'),
    path('date/', viewss.ServerDate, name='date'),
    path('', include(router.urls)),
]