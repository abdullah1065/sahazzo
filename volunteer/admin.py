from django.contrib import admin
from volunteer.models import  VolunteerTable
# Register your models here.

class VolunteerTableAdmin(admin.ModelAdmin):
    list_display = ('V_ID', 'EMAIL', 'STATUS', 'VOLUNTARY')
admin.site.register(VolunteerTable, VolunteerTableAdmin)


