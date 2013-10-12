from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import simplejson
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    return render(request, 'accounts/sign-up.html')


@csrf_exempt
def signedup(request):
    response = {}
        
    if request.is_ajax():
        if request.method == 'POST':
            userjson = simplejson.loads(request.raw_post_data)            

            try:
                u = User.objects.get(username__exact=userjson['userName'])
            except User.DoesNotExist:
                user = User.objects.create_user(userjson['userName'],userjson['email'], userjson['password']);
                user.last_name = userjson['lastName']
                user.first_name = userjson['firstName']
                user.save();
                response['message'] = 'Success'
                response['redirect'] = reverse('accounts:landing')
                return HttpResponse(simplejson.dumps(response))
            else:
                
                response['message'] = 'User already present'
                return HttpResponse(simplejson.dumps(response))
    
    response['message'] = 'failure'
    return HttpResponse(simplejson.dumps(response))

@login_required
def landing(request):
    return render(request, 'accounts/welcome.html')


def login(request):
    return render(request, 'accounts/sign-in.html')

@csrf_exempt
def loggedin(request):
    response = {}
    
    if request.is_ajax():
        if request.method == 'POST':
            userjson = simplejson.loads(request.raw_post_data)
            
            """"TODO: check if user already exists"""
            user = authenticate(username=userjson['userName'], password=userjson['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    auth_login(request, user)
                    response['message'] = 'Success'
                    response['redirect'] = reverse('accounts:landing')
                    return HttpResponse(simplejson.dumps(response))
                
    response['message'] = 'Unknown username or password'    
    return HttpResponse(simplejson.dumps(response))

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def info(request):
    response = {}
    
    user = request.user;
    
    response['userName'] = user.username
    response['firstName'] = user.first_name
    response['lastName'] = user.last_name
    response['email'] = user.email

    return HttpResponse(simplejson.dumps(response))

@login_required
def updateInfo(request, user_id):
    response = {}
    
    if request.is_ajax():
        if request.method == 'POST':
            userjson = simplejson.loads(request.raw_post_data)    

            u = request.user
            u.first_name = userjson['firstName']
            u.last_name = userjson['lastName']
            u.email = userjson['email']
            u.save()
            
            response['message'] = 'Success'
            return HttpResponse(simplejson.dumps(response))
    
    response['message'] = 'failure'
    return HttpResponse(simplejson.dumps(response))    
