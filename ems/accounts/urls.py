from django.urls import path
from .import views


app_name = 'accounts'

urlpatterns = [
    # testing views
    #path('users/blocked/all',views.users_blocked_list,name='erasedusers'),
    path('login/',views.loginpage,name="login"),
    # path('register/',views.registerpage,name='register'),
    # path('register/',views.registerpage,name='register'),

    path('logout/',views.logout_view,name='logout'),
    path('users/all',views.users_list,name='users'),
    path('users/<int:id>/block',views.users_block,name='userblock'),
    path('users/<int:id>/unblock',views.users_unblock,name='userunblock'),
    path('users/blocked/all',views.users_blocked_list,name='erasedusers'),
    path('users/Update_user',views.update_uesr,name='Update_user'),
    path('profile_list', views.profile_list, name = "profile_list"),
    # path <int:pk> -> interger pramary key
    path('profile/<int:pk>', views.profile, name = "profile"),
    path('register/',views.register_user,name='register'),
]

