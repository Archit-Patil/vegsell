from django.contrib import admin
from .models.product import Product
from .models.category import Category


class AdminProduct(admin.ModelAdmin):
    list_display =['name','price','category','description']

admin.site.register(Product,AdminProduct)
class AdminCategory(admin.ModelAdmin):
    list_display =['name']

admin.site.register(Category,AdminCategory)
# Register your models here.
