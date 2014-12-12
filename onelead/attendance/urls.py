from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from attendance import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^addattendance', views.add_attendance, name='add_attendance'),
		url(r'^getslots.json', views.get_slots, name='get_slots'),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

