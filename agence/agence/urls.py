from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from catalogue.views import home



urlpatterns = patterns('',
	 url(r'^$', home),
    url(r'^catalog/', include('catalogue.urls', namespace="catalog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
