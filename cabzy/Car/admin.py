from django.contrib import admin
from .models import Car, Car_location, ride
# Register your models here.

admin.site.register(Car)
admin.site.register(Car_location)
admin.site.register(ride)