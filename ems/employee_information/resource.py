from import_export import resources 
from .models import Employees


class PersonResources(resources.ModelResource):
    class meta:
        model = Employees