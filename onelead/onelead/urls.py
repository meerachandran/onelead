from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	url(r'^attendance/', include('attendance.urls')),
	url(r'^example/', include('example.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^leadadmin/', include('leadadmin.urls')),
	url(r'^batch/', include('batch.urls')),
	url(r'^faculty/', include('faculty.urls')),
	url(r'^timetable/', include('timetable.urls')),
	url(r'^student/', include('student.urls')),
	url(r'^faculty/', include('faculty_dashboard.urls')),

)
