from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
     url(r'^signup$', views.signup, name='signup'),
     url(r'^signedup$', views.signedup, name='signuped'),
     url(r'^landing', views.landing, name='landing'),
)