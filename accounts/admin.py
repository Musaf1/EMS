from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import Group,User


# Register your models here.

# unergester user
admin.site.unregister(User)

# unergester Group
admin.site.unregister(Group)

# Get the Profile table
class ProfileInine(admin.StackedInline): 
    model = Profile
    
# create new user with spicfic tables and include profile with it 
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username","first_name","last_name","last_login","email","is_active","is_staff","is_superuser"]
    inlines = [ProfileInine]
# register user to render in admin page
admin.site.register(User,UserAdmin)
