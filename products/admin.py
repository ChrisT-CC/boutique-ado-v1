"""Product app admin file"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Product model"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    # Sort the products by SKU using the ordering attribute
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Categoriy model"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
