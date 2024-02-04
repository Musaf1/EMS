from django.contrib import admin
from employee_information.models import Department, Position, Employees,attendace
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field

#export from view 
class exportForm(resources.ModelResource):
    # name = Field() if name is FK then use this 
    class Meta:
        model = attendace
        fields = ( 'name', 'date','Time_attendace', 'time_leaves','total_time')
        export_order = fields # same or change the order 

    # this part to get the FK data rather than 1 
    '''
    def dehydrate_name(self,obj) :
        return str(obj.name.username)
    '''
#expot form admin page
class exportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = exportForm
# uplode exile by admin page 
admin.site.register(Employees)
class userdat(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
#admin.site.register(Employees)
admin.site.register(attendace,exportAdmin)
 
