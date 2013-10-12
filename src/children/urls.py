from django.conf.urls import patterns, url

from children import views

urlpatterns = patterns('',
     url(r'^$', views.mychildren, name='mychildren'),
     url(r'^addChild/$', views.createchild, name='createchild'),
     
)