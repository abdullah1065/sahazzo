from django.contrib import admin
from home.models import PersonTable
# Register your models here.
class PersonTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'PersonType', 'FIRST_NAME','LAST_NAME','EMAIL','CONTACT','NID','PASSWORD', 'CONFIRM_PASSWORD')
admin.site.register(PersonTable, PersonTableAdmin)


