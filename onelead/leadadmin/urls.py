from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from leadadmin import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
