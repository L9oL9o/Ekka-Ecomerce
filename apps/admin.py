from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import *


class ColorInline(admin.TabularInline):
    model = Color


class PriceInline(admin.TabularInline):
    model = Price


class SizeInline(admin.TabularInline):
    model = Size


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'get_colors', 'get_prices', 'get_sizes']
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ColorInline, PriceInline, SizeInline]

    def get_colors(self, obj):
        return ', '.join([color.name for color in obj.color.all()])
    get_colors.short_description = 'Colors'

    def get_prices(self, obj):
        return ', '.join([f"{price.size.name} - {price.color.name} : {price.price}" for price in obj.price.all()])
    get_prices.short_description = 'Prices'

    def get_sizes(self, obj):
        return ', '.join([size.name for size in obj.size.all()])
    get_sizes.short_description = 'Sizes'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('color', 'price__size')



@admin.register(Color)
class ColorAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Price)
class PriceAdmin(ModelAdmin):
    list_display = ['id', 'price']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['id', 'name', 'text']
    list_display_links = ['id', 'name', 'text']


@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin):
    list_display = ['id']
