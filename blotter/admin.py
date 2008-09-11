from django.contrib import admin
from blotter.models import CrimeType, Agency, Crime

class CrimeTypeAdmin(admin.ModelAdmin):
    model = CrimeType
    prepopulated_fields={'slug':('type',)}

class AgencyAdmin(admin.ModelAdmin):
    model = Agency
    prepopulated_fields={'slug':('name',)}

class CrimeAdmin(admin.ModelAdmin):
    exclude = ['latitude', 'longitude']

admin.site.register(CrimeType, CrimeTypeAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Crime, CrimeAdmin)
