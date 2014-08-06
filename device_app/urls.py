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
	# mostrar aplicaciones
	url(r'^applications/$', 'device_app.views.applications', name="applications"),
	# logout
	url(r'^logout/$', 'device_app.views.logOut', name='logout'),
	# dispositivo
	url(r'^device/id/(?P<id>\d+)/(.+)$', 'device_app.views.device' , name="device"),
	# Aplicacion
	url(r'^app/id/(?P<id>\d+)/(.+)$', 'device_app.views.app' , name="app"),
	# detalles Devices
	url(r'^detailsDevice/id/(?P<id>\d+)/(.+)$', 'device_app.views.detailsDevice' , name="detailsDevice"),
	# detalles Apps
	url(r'^detailsApps/id/(?P<id>\d+)/(.+)$', 'device_app.views.detailsApps' , name="detailsApps"),
	# instalar Apps
	url(r'^installAppInicio/$', 'device_app.views.installAppInicio' , name="installAppInicio"),
	# instalar Apps - especifica
	url(r'^installApp2/id/(?P<id>\d+)/(.+)$', 'device_app.views.installApp2' , name="installApp2"),	
	# buscar
	url(r'^buscarApp/$', 'device_app.views.buscarApp' , name="buscarApp"),
	)