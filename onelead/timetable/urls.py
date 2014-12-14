from django.conf.urls import patterns, url,include

from timetable import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
     url(r'^getslots$', views.get_slots, name='get_slots')
    )+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
