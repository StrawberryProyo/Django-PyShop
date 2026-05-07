from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('prodname', 'price', 'stock', 'description')
	search_fields = ('prodname', 'description')
