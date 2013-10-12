from django.http import HttpResponse
from django.contrib.auth.models import User
from children.models import Child
from django.shortcuts import get_list_or_404,get_object_or_404
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import simplejson 



def index(request):
    return HttpResponse("Hello, world. You're at the children index.")

@login_required
def mychildren(request):
    usr = request.user
    children=get_list_or_404(Child,parent=usr)
    children_as_json = serializers.serialize('json', children);
    return HttpResponse(children_as_json, content_type='json')

@login_required
def createchild(request):
    if request.method == 'POST':
            userjson = simplejson.loads(request.raw_post_data)
            
            """"TODO: check if user already exists"""
            usr = request.user
    Child.objects.add_child(userjson['fname'],userjson['lname'],userjson['mname'],userjson['gender'],userjson['bdate'],usr) 
    return HttpResponse(status=201)
    
    




