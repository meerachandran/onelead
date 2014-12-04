from django.conf.urls import patterns, url

from example import views

urlpatterns = patterns('',
    url(r'^batchformsimple', views.batch_form_simple, name='batch_form_simple'),
    url(r'^batchform', views.batch_form, name='batch_form'),
    url(r'^printdb', views.print_db, name='print_db'),
)
