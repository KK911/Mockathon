from django.conf.urls import patterns, url

from children import views

urlpatterns = patterns('',
     url(r'^(?P<parent_id>\d+)/$', views.mychildren, name='mychildren'),
     
)