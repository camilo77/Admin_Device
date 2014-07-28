from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Admin_Device.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('device_app.urls', namespace = "device_app")),
    url(r'^admin/', include(admin.site.urls)),
)
