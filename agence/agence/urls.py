from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.flatpages import views




urlpatterns = patterns('',
	url(r'^$', views.flatpage, {'url': '/'}, name='home'),	
    url(r'^catalog/', include('catalogue.urls', namespace="catalog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^contact/$', views.flatpage, {'url': '/contact/'}, name='contact'),
    #url(r'^$', views.flatpage, {'url': '/home/'}, name='home'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
