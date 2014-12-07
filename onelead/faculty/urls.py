from django.conf.urls import patterns, url

from example import views

urlpatterns = patterns('',
    url(r'^addfaculty', views.batch_form_simple, name='add_faculty'),
)
