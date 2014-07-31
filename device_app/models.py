from django.db import models

# Create your models here.

class Device(models.Model):
	name = models.CharField(max_length=100, unique=True)
	ip = models.CharField(max_length=12, unique=True)
	status = models.CharField(max_length=10)
	tipo = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Application(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class DeviceApp(models.Model):
	device = models.ForeignKey(Device)
	aplication = models.ForeignKey(Application)
	status = models.CharField(max_length=10)

	def __str__(self):
		return self.device.name +' '+ self.aplication.name	