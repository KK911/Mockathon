from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
     url(r'^signup$', views.signup, name='signup'),
     url(r'^signedup$', views.signedup, name='signuped'),
     url(r'^landing', views.landing, name='landing'),
     url(r'^login$', views.login, name='login'),
     url(r'^loggedin$', views.loggedin, name='loggedin'),
     url(r'^logout', views.logout, name='logout'),
     url(r'^info', views.info, name='info'),
)