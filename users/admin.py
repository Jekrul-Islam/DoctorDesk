from django.contrib import admin
from .models import appointment,patient,contact
# Register your models here.
admin.site.register(appointment)
admin.site.register(patient)
admin.site.register(contact)
