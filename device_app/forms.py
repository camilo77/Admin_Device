from django import forms
from models import Device, Application, DeviceApp

TYPE_CHOICES = (
	('PC.jpg', 'PC'),
	('Cel.png', 'Celular'),
	('Tablet.jpg', 'Tableta'),
)
class NewDeviceForm(forms.Form):
	nombre = forms.CharField()
	tipo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=TYPE_CHOICES)
	ip = forms.IntegerField()
	aplicaciones = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
		queryset=Application.objects.all(), required=False)

class NewUser(forms.Form):
	nombre = forms.CharField()
	apellido = forms.CharField()
	correo = forms.EmailField()
	usuario = forms.CharField()
	contrasena = forms.CharField(widget = forms.PasswordInput())

class LogForm(forms.Form):
	usuario = forms.CharField()
	contrasena = forms.CharField(widget = forms.PasswordInput()) 

class NewAppForm(forms.Form):
	nombre = forms.CharField()