from django.conf.urls import patterns, include, url
from tastypie.api import api
from children.api.resources import MyChildResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoseed.views.home', name='home'),
    # url(r'^djangoseed/', include('djangoseed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^settings/children', 'children.views.index'),
    
    url(r'^children/', include('children.urls', namespace="children")),
    
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    
    url(r'^accounts/login/', 'accounts.views.login'),    
    
)
