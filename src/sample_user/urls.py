from django.conf.urls import patterns, url

from sample_user import views

urlpatterns = patterns('',
#     url(r'^$', views.index, name='index'),
#     url(r'^specifics/(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),    
    url(r'^$', views.index, name='index'),    
    
)