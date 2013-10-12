from django.http import HttpResponse
from django.contrib.auth.models import User
from children.models import Child
from django.shortcuts import get_list_or_404,get_object_or_404
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the children index.")
def mychildren(request, parent_id):
    children=get_list_or_404(Child,parent=get_object_or_404(User,pk=parent_id))
    children_as_json = serializers.serialize('json', children);
    return HttpResponse(children_as_json, content_type='json')
    
    




