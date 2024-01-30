from django.contrib import admin
from order.models import Order
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name','email','order_details', 'is_completed']
    list_filter = ['customer_name','email','is_completed']
    search_fields = ['customer_name','email']
    list_editable = ['is_completed']