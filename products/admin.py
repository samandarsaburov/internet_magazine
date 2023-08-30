from django.contrib import admin
from .models import ProductsModel
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= ['title','description','price','category','image','create_at']
    search_fields =['title']
    
admin.site.register(ProductsModel,ProductAdmin)
