from django.conf.urls import patterns, url,include

from timetable import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),)
