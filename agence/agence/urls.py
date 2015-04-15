from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from catalogue.views import home
from django.contrib.auth import views as auth_views




urlpatterns = patterns('',
	 url(r'^$', home),
    url(r'^catalog/', include('catalogue.urls', namespace="catalog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^accounts/login/$', auth_views.login),
    #url('^', include('django.contrib.auth.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
