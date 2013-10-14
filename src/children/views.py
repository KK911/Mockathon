from django.http import HttpResponse
from children.models import Child
from django.shortcuts import get_list_or_404
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'children/children.html')

@login_required
def mychildren(request):
    usr = request.user
    children=get_list_or_404(Child,parent=usr)
    children_as_json = serializers.serialize('json', children);
    return HttpResponse(children_as_json, content_type='json')
       
@csrf_exempt
def createchild(request):
    if request.method == 'POST':
            userjson = simplejson.loads(request.raw_post_data)
            
            """"TODO: check if user already exists"""
            usr = request.user
    Child.objects.add_child(userjson['fname'],userjson['lname'],userjson['mname'],userjson['gender'],userjson['bdate'],usr) 
    return HttpResponse(status=201)

def addchild(request):
    return render(request, 'children/addchild.html')
    
    




