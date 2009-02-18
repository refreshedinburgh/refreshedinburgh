from django.conf.urls.defaults import handler404, handler500, include, patterns
from django.conf import settings
from django.contrib import admin

import settings


admin.autodiscover()


urlpatterns = patterns('',
    (r'^', include('apps.core.urls')),
    (r'^events/', include('apps.events.urls')),
    (r'^admin/', include(admin.site.urls)),
)


if settings.SERVER_ENV == 'development':
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

