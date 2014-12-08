from django.conf.urls import patterns, url

from faculty import views

urlpatterns = patterns('',
		url(r'^addfaculty', views.add_faculty, name='add_faculty'),
)
