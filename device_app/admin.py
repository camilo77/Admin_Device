from django.contrib import admin
from device_app.models import Device, Application, DeviceApp

# Register your models here.

admin.site.register(Device)
admin.site.register(Application)
admin.site.register(DeviceApp)
