from django.contrib import admin
from organizor.models import OrganizorTable, EventTable,  ShopTable
# Register your models here.


class OrganizorTableAdmin(admin.ModelAdmin):
    list_display = ('O_ID', 'EMAIL')
admin.site.register(OrganizorTable, OrganizorTableAdmin)

class EventTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'EVENT_NAME', 'START_TIME', 'END_TIME', 'LOCATION', 'BUDGET', 'SHOP', 'ITEMS', 'QUANTITY', 'EVENT_FOR', 'CREATED_BY')
admin.site.register(EventTable, EventTableAdmin)

class ShopTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'SHOP_NAME', 'PAY_DEMAND', 'DELIVERY_STATUS')
admin.site.register(ShopTable, ShopTableAdmin)

