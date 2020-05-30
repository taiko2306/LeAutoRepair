from django.contrib import admin
from .models import Vehicle, Service, Profile

admin.site.register(Vehicle)
admin.site.register(Service)
admin.site.register(Profile)