from django.conf.urls import patterns, url

from catalogue import views

urlpatterns = patterns('',
   url(r'^$', views.index, name='index'), 
   url(r'^company/(?P<company_id>\d+)/$', views.detail_company, name='detail_company'),   
   url(r'^scene/(?P<scene_id>\d+)/$', views.detail_scene, name='detail_scene'),   
)
