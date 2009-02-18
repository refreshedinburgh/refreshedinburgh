from django.conf.urls.defaults import handler404, handler500, include, patterns


urlpatterns = patterns('',
    (r'^events/', include('apps.events.urls')),
)