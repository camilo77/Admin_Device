from django.conf.urls import patterns, url
from device_app.views import inicio,register, newDevice, newApplication,devices


urlpatterns = patterns('',
	url(r'^$', 'device_app.views.inicio', name='inicio'),
	url(r'^register/$', 'device_app.views.register', name= 'register'),
	url(r'^newDevice/$', 'device_app.views.newDevice', name = 'newDevice'),
	url(r'^newApplication/$', 'device_app.views.newApplication', name="newApplication"),
	url(r'^devices$', 'device_app.views.devices', name="devices"),
	)