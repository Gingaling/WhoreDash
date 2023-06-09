from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['category']
    # date_hierarchy = 'created'
    # ordering = ['name', 'price']
