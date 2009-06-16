from django.conf.urls.defaults import include, patterns, url

import views


urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^members/$', views.members, name='member_list'),
    url(r'^jobs/$', views.jobs, name='job_list'),
)
