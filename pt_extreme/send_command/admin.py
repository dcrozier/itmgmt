from django.contrib import admin
from .models import Credentials, Site, Interface, NetworkDevice

# Register your models here.

admin.site.register(Credentials)
admin.site.register(Site)
admin.site.register(Interface)
admin.site.register(NetworkDevice)
