from django.contrib import admin
from .models import Vehicle, Service, User_Profile, Profile

admin.site.register(Vehicle)
admin.site.register(Service)
admin.site.register(User_Profile)
admin.site.register(Profile)