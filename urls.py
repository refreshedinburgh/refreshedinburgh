from django.conf.urls.defaults import handler404, handler500, include, patterns
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^events/', include('apps.events.urls')),
    ('^admin/', include(admin.site.urls)),
)