from django.shortcuts import render
from django.shortcuts import render_to_response
from forms import NewDeviceForm, NewUser, LogForm, NewAppForm
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from models import Device, Application

# Create your views here.

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
					return HttpResponseRedirect(reverse('device_app:devices'),request)
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

def register(request):
	if request.method == 'POST':
		form = NewUser(request.POST)
		if form.is_valid():
			username = form.cleaned_data["usuario"]

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


def newDevice(request):
	if request.method == 'POST':
		form = NewDeviceForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			tipo = form.cleaned_data['tipo']
			ip = form.cleaned_data['ip']
			

			if not Device.objects.filter(name=nombre):
				newDevice = Device(name=nombre,ip=ip,tipo=tipo,status='ON')
				newDevice.save()
			
			form = NewDeviceForm()
			context = {
			'formulario':form,
			}
			return render_to_response('newDevice.html', context, context_instance=RequestContext(request))
	else:
		form = NewDeviceForm()
		context = {
		'formulario':form,
		}
		return render_to_response('newDevice.html',context, context_instance=RequestContext(request))

def newApplication(request):
	if request.method == 'POST':
		form = NewAppForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']

			if not Application.objects.filter(name = nombre):
				newApplication = Application(name=nombre)
				newApplication.save()
			form = NewAppForm()
			context = {
			'formulario':form,
			}
			return render_to_response('newApplication.html', context, context_instance=RequestContext(request))
	else:
		form = NewAppForm()
		context = {
		'formulario':form,
		}
		return render_to_response('newApplication.html',context,context_instance=RequestContext(request))

@login_required()
def devices(request):
	devices = Device.objects.all()
	context = {
	'estado': 'checked',
	'devices': devices,
	'user': request.user,
	}
	return render_to_response('devices.html',context)