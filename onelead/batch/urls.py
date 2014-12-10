from django.conf.urls import patterns, url

from batch import views

urlpatterns = patterns('',
    url(r'^batchform', views.batch_form, name='batch_form'),
)
