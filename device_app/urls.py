from django.conf.urls import patterns, url

from device_app import views

urlpatterns = patterns('',
	url(r'^$', views.inicio, name = 'inicio'),
	url(r'^register/$', views.register, name= 'register'),
	url(r'^newDevice/$', views.newDevice, name = 'newDevice'),
	url(r'^newApplication/$', views.newApplication, name="newApplication"),
	url(r'^devices$', views.devices, name="devices"),
	)