from django.contrib import admin
from .models import OrderModel

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','tel','yashash_joyi','order_name','create_at']
    search_fields = ['name','order_name']

admin.site.register(OrderModel,OrderAdmin)
