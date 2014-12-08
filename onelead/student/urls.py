from django.conf.urls import patterns, url

from student import views

urlpatterns = patterns('',
    url(r'^addstudent', views.add_student, name='add_student'),
)
