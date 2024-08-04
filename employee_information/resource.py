from import_export import resources 
from .models import Employees_info


class PersonResources(resources.ModelResource):
    class meta:
        model = Employees_info