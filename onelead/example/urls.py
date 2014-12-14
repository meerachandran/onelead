from django.conf.urls import patterns, url,include

from example import views
from example.api import EntryResource


entry_resource = EntryResource()

urlpatterns = patterns('',
    url(r'^batchformsimple', views.batch_form_simple, name='batch_form_simple'),
    url(r'^batchform', views.batch_form, name='batch_form'),
    url(r'^printdb', views.print_db, name='print_db'),
)
