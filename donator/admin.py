from django.contrib import admin
from donator.models import DonatorTable,  DonateTable, FundTable
# Register your models here.

class DonatorTableAdmin(admin.ModelAdmin):
    list_display = ('D_ID', 'EMAIL')
admin.site.register(DonatorTable, DonatorTableAdmin)

class DonateTableAdmin(admin.ModelAdmin):
    list_display = ('D_ID' , 'EVENT_ID', 'PAYMENT_DETAILS', 'PAYMENT')
admin.site.register(DonateTable, DonateTableAdmin)

class FundTableAdmin(admin.ModelAdmin):
    list_display = ('EVENT_ID', 'COLLECTED_AMOUNT', 'FUND_STATUS', 'FUND_TAKEN_BY')
admin.site.register(FundTable, FundTableAdmin)

