from django.conf.urls.defaults import include, patterns

import views


urlpatterns = patterns('',
    (r'^$', views.home),
)
