from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from models import Device, Application, DeviceApp
from forms import NewDeviceForm, NewUser, LogForm, NewAppForm, installAppForm

# Create your views here.
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# login
def inicio(request):
	if request.method == 'POST':
		form = LogForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["usuario"]
			password = form.cleaned_data["contrasena"]
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('device_app:appsDevices'),request)
				else:
					return HttpResponseRedirect(reverse('device_app:inicio'))
			else:
				form = LogForm()
		    	context = {
		    	'formulario':form,
		    	'mensaje':'usuario y/o contrasena invalido'
		    	}
		    	return render_to_response('inicio.html',context,context_instance=RequestContext(request))
	else:
		form = LogForm()
    	context = {
    	'formulario':form,
    	}
    	return render_to_response('inicio.html',context,context_instance=RequestContext(request))

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def logOut(request):
	logout(request)
	return HttpResponseRedirect(reverse('device_app:inicio'))

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def register(request):
	if request.method == 'POST':
		form = NewUser(request.POST)
		if form.is_valid():
			username = form.cleaned_data["usuario"]

			# si el usuario no existe se crea
			if not User.objects.filter(username = username):
				
				password = form.cleaned_data["contrasena"]
				email = form.cleaned_data["correo"]
				first_name = form.cleaned_data["nombre"]
				last_name = form.cleaned_data["apellido"]

				user = User.objects.create_user(username, email, password)
				user.first_name = first_name
				user.last_name = last_name
				user.save()
				# toca cambiar posteriormente el retorno para que el usuario quede logeado directamente
				return HttpResponseRedirect(reverse('device_app:inicio'))
			else:
				context = {
				'formulario':form,
				'mensaje':'El Usuario ya existe'
				}
				return render_to_response('register.html',context,context_instance=RequestContext(request))
		else:
			form = NewUser()
			context = {
			'formulario':form,
			'mensaje':'Registre los datos correctamente'
			}
			return render_to_response('register.html',context,context_instance=RequestContext(request))
	else:
		form = NewUser()
		context = {
		'formulario':form,
		}
		return render_to_response('register.html',context,context_instance=RequestContext(request))

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@login_required(login_url='device_app:inicio')
def newDevice(request):
	if request.method == 'POST':
		form = NewDeviceForm(request.POST)
		if form.is_valid():
			
			nombre = form.cleaned_data['nombre']
			tipo = form.cleaned_data['tipo']
			ip = form.cleaned_data['ip']
			aplicacion = form.cleaned_data['aplicaciones']

			if not Device.objects.filter(name=nombre) and not Device.objects.filter(ip=ip):
				newDevice = Device(name=nombre,ip=ip,tipo=tipo,status='ON')
				newDevice.save()

				if aplicacion:
					newDeviceApp = DeviceApp(device=newDevice,aplication=aplicacion,status='ON')
					newDeviceApp.save()

				form = NewDeviceForm()
				context = {
				'formulario':form,
				'mensaje':'Dispositivo creado con exito',
				}
				return render_to_response('newDevice.html', context, context_instance=RequestContext(request))
			else:
				form = NewDeviceForm()
				context = {
				'formulario':form,
				'mensaje':'Nombre o ip de dispositivo ya existente',
				}
				return render_to_response('newDevice.html', context, context_instance=RequestContext(request))
		else:
			form = NewDeviceForm()
			context = {
			'formulario':form,
			'mensaje':'Registre los datos correctamente',
			}
			return render_to_response('newDevice.html', context, context_instance=RequestContext(request))
	else:
		form = NewDeviceForm()
		context = {
		'formulario':form,
		}
		return render_to_response('newDevice.html',context, context_instance=RequestContext(request))

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@login_required(login_url='device_app:inicio')
def newApplication(request):
	if request.method == 'POST':
		form = NewAppForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			nombre = nombre.lower()
			if not Application.objects.filter(name = nombre):
				newApplication = Application(name=nombre)
				newApplication.save()
			form = NewAppForm()
			context = {
			'formulario':form,
			'mensaje':'Aplicaion creada con exito',
			}
			return render_to_response('newApplication.html', context, context_instance=RequestContext(request))
	else:
		form = NewAppForm()
		context = {
		'formulario':form,
		'mensaje':'Registre los datos correctamente',
		}
		return render_to_response('newApplication.html',context,context_instance=RequestContext(request))

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@login_required(login_url='device_app:inicio')
def appsDevices(request):
	devices = Device.objects.all()
	applications = Application.objects.all()
	context = {
	'devices': devices,
	'applications': applications,
	'user': request.user,
	}
	return render_to_response('appsDevices.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@login_required(login_url='device_app:inicio')
def devices(request):
	devices = Device.objects.all()
	context = {
	'devices': devices,
	'user': request.user,
	}
	return render_to_response('devices.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@login_required(login_url='device_app:inicio')
def applications(request):
	applications = Application.objects.all()
	context = {
	'applications': applications,
	'user': request.user,
	}
	return render_to_response('applications.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def device(request,id):
	dispositivo = Device.objects.filter(id=id)[0]
	aplicaciones = DeviceApp.objects.filter(device=dispositivo)
	context = {
	'device':dispositivo,
	'apps':aplicaciones,
	'user': request.user,
	}
	return render_to_response('device.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def app(request,id):
	aplicacion = Application.objects.filter(id=id)[0]
	dispositivos = DeviceApp.objects.filter(aplication=aplicacion)
	context = {
	'app':aplicacion,
	'devices':dispositivos,
	'user': request.user,
	}
	return render_to_response('app.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def detailsDevice(request,id):
	dispositivo = Device.objects.filter(id=id)[0]
	context = {
	'device':dispositivo,
	'user': request.user,
	}
	return render_to_response('detailsDevice.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def detailsApps(request,id):
	app = Application.objects.filter(id=id)[0]
	context = {
	'app':app,
	'user': request.user,
	}
	return render_to_response('detailsApps.html',context)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def buscarApp(request):
	if request.method == 'POST':
		nombre = request.POST['buscar']
		if Application.objects.filter(name__contains=nombre):
			aplicaciones = Application.objects.filter(name__contains=nombre)

			context = {
			'applications': aplicaciones,
			'user': request.user,
			'mensaje': 'Coincidencias con '+ '"'+nombre+'"'
			}
			return render_to_response('installApp.html', context, context_instance=RequestContext(request))
		else:
			aplicaciones = Application.objects.filter(name__contains=nombre)
			context = {
			'applications': aplicaciones,
			'user': request.user,
			'mensaje': 'No se encontro ninguna Aplicacion con nombre '+ '"'+nombre+'"'
			}
			return render_to_response('installApp.html', context, context_instance=RequestContext(request))


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@login_required(login_url='device_app:inicio')
def installAppInicio(request):
	applications = Application.objects.all()
	context = {
	'applications': applications,
	'user': request.user,
	}
	return render_to_response('installApp.html', context, context_instance=RequestContext(request))


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def installApp2(request,id):
	if request.method == 'POST':
		form = installAppForm(request.POST)
		if form.is_valid():

			nameDispositivo = form.cleaned_data['dispositivo']
			aplicacion = Application.objects.filter(id=id)[0]
			device = Device.objects.filter(name=nameDispositivo)[0]

			newDeviceApp = DeviceApp(device=device,aplication=aplicacion,status='OFF')

			if not DeviceApp.objects.filter(device=device, aplication=aplicacion):
				newDeviceApp.save()
				app = Application.objects.filter(id=id)[0]
				devices = Device.objects.all()
				context = {
				'app':app,
				'devices': devices,
				'user': request.user,
				'mensaje': 'Aplicacion "'+aplicacion.name+'" instalada exitosamente en Dispositivo: "'+nameDispositivo+'"'
				}
				return render_to_response('installApp2.html',context, context_instance=RequestContext(request))
			else:
				app = Application.objects.all()
				devices = Device.objects.all()
				context = {
				'applications':app,
				'devices': devices,
				'user': request.user,
				'mensaje': 'Aplicacion "'+aplicacion.name+'" ya esta instalada en Dispositivo: "'+nameDispositivo+'"'
				}
				return render_to_response('installApp.html', context, context_instance=RequestContext(request))
	else:
		app = Application.objects.filter(id=id)[0]
		devices = Device.objects.all()
		context = {
		'app':app,
		'devices': devices,
		'user': request.user,
		}
		return render_to_response('installApp2.html',context, context_instance=RequestContext(request))