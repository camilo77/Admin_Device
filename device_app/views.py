from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def inicio(request):
	return render_to_response('inicio.html')

def register(request):
	return render_to_response('register.html')

def newDevice(request):
	return render_to_response('newDevice.html')

def newApplication(request):
	return render_to_response('newApplication.html')

def devices(request):
	return render_to_response('devices.html',{'estado': 'checked'})