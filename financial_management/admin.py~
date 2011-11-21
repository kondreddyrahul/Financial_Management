from financial_management.models import Customer
from financial_management.models import MutualFund
from financial_management.models import IPO
from financial_management.models import FO
from financial_management.models import Admin
from financial_management.models import account

from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    fields = ['customer_Name', 'customer_ID']
    list_display = ('customer_Name', 'customer_ID')
    list_filter = ['customer_Name', 'customer_ID']
    search_fields = ['customer_Name', 'customer_ID']
class MutualFundAdmin(admin.ModelAdmin):
    fields = ['mf_Name', 'mf_ID', 'mf_Qty', 'mf_cost']
    list_display = ('mf_Name', 'mf_ID', 'mf_Qty', 'mf_cost')
    list_filter = ('mf_Name', 'mf_ID', 'mf_Qty', 'mf_cost')
class IPOAdmin(admin.ModelAdmin):
    fields = ['ipo_Name', 'ipo_ID', 'ipo_Qty', 'ipo_cost']
    list_display = ('ipo_Name', 'ipo_ID', 'ipo_Qty', 'ipo_cost')
    list_filter = ('ipo_Name', 'ipo_ID', 'ipo_Qty', 'ipo_cost')
class FOAdmin(admin.ModelAdmin):
    fields = ['fo_Name', 'fo_ID', 'fo_Qty', 'fo_cost']
    list_display = ('fo_Name', 'fo_ID', 'fo_Qty', 'fo_cost')
    list_filter = ('fo_Name', 'fo_ID', 'fo_Qty', 'fo_cost')
class AdminAdmin(admin.ModelAdmin):
    fields = ['admin_Name', 'admin_ID']
    list_display = ('admin_Name', 'admin_ID')
    list_filter = ('admin_Name', 'admin_ID')
class accountAdmin(admin.ModelAdmin):
    fields = ['user_id', 'tot_bal', 'mf_bal', 'po_bal', 'fo_bal']
    list_display = ('user_id', 'tot_bal', 'mf_bal', 'po_bal', 'fo_bal')
    list_filter = ['user_id', 'tot_bal', 'mf_bal', 'po_bal', 'fo_bal']
    search_fields = ['user_id', 'tot_bal', 'mf_bal', 'po_bal', 'fo_bal']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(MutualFund, MutualFundAdmin)
admin.site.register(IPO, IPOAdmin)
admin.site.register(FO, FOAdmin)
admin.site.register(Admin,AdminAdmin)
admin.site.register(account,accountAdmin)