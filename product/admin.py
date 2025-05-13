from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'category', 'created_at')
    list_filter = ('is_available', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_available')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'price', 'stock', 'is_available')
        }),
        ('Category', {
            'fields': ('category',)
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
