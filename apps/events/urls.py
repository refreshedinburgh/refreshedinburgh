from django.conf.urls.defaults import patterns, url

from apps.events import views


urlpatterns = patterns('',
    url('^$', views.event_archive, name='events_event_archive'),
    url('^(?P<year>\d{4})/$', views.event_year_archive,
        name='events_event_year_archive'),
    url('^(?P<year>\d{4})/(?P<slug>.+)/$', views.event_detail,
        name='events_event_detail'),
)
