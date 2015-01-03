from django.conf.urls import patterns, url,include

from faculty_dashboard import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^batchlist$', views.batch_list, name='batch_list'),
    url(r'^studentlist/(?P<batchid>\d+)/$', views.student_list, name='student_list'),
    url(r'^batchmaps/(?P<staffid>\d+)/$', views.batch_maps, name='batch_maps'),
    )+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
