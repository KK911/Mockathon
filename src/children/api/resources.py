from tastypie.resources import ModelResource
from children.models import Child


class MyChildResource(ModelResource):
    class Meta:
        queryset = Child.objects.all()
        allowed_methods = ['get']