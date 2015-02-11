from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalogue import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<scene_id>\d+)/$', views.detail, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
