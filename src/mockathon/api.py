

from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from children.models import Child
from diapers.models import Diaper

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        
class ChildResource(ModelResource):
    parent = fields.ForeignKey(UserResource, 'parent')
    
    class Meta:
        queryset = Child.objects.all()
        resource_name = 'children'
        
class DiaperResource(ModelResource):
    child = fields.ForeignKey(ChildResource, 'child')
    
    class Meta:
        queryset = Diaper.objects.all()
        resource_name = 'diapers'                

