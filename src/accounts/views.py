from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import simplejson
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    return render(request, 'accounts/sign-up.html')

@csrf_exempt
def signedup(request):
    response = {}
        
    if request.is_ajax():
        if request.method == 'POST':
            userjson = simplejson.loads(request.raw_post_data)
            
            """"TODO: check if user already exists"""
            try:
                u = User.objects.get(username__exact=userjson['userName'])
            except User.DoesNotExist:
                user = User.objects.create_user(userjson['userName'],userjson['email'], userjson['password']);
                user.last_name = userjson['lastName']
                user.first_name = userjson['firstName']
                user.save();
                response['message'] = 'Success'
                response['Redirect'] = reverse('accounts:landing')
            else:
                
                response['message'] = 'User already present'
                return HttpResponse(simplejson.dumps(response))
    
    return HttpResponse(simplejson.dumps(response))

def landing(request):
    return render(request, 'accounts/landing.html')