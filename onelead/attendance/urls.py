from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from attendance import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^getslots', views.get_slots, name='get_slots'),
		url(r'^addstudents', views.add_students, name='add_students'),
    url(r'^submitstudents', views.submit_students, name='submit_students'),
    url(r'^addbatch', views.submit_students, name='add_batch'),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
