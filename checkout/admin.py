from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem
    
class OrderAmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    
admin.site.register(Order, OrderAmin)
