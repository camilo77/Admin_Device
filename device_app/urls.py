from django.conf.urls import patterns, url
from device_app.views import inicio,register, newDevice, newApplication,devices


urlpatterns = patterns('',
	# pagina inicio y login
	url(r'^$', 'device_app.views.inicio', name='inicio'),
	# registrar usuario nuevo
	url(r'^register/$', 'device_app.views.register', name= 'register'),
	#pagina principal - muestra apps y devices
	url(r'^appsDevices/$', 'device_app.views.appsDevices', name= 'appsDevices'),
	# registrar nuevo dispositivo
	url(r'^newDevice/$', 'device_app.views.newDevice', name = 'newDevice'),
	# registrar nueva aplicacion
	url(r'^newApplication/$', 'device_app.views.newApplication', name="newApplication"),
	# mostrar dispositivos
	url(r'^devices/$', 'device_app.views.devices', name="devices"),
	# logout
	url(r'^logout/$', 'device_app.views.logOut', name='logout'),
	)