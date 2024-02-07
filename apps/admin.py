from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from apps.models import *


class ColorInline(TabularInline):
    model = Color


class PriceInline(TabularInline):
    model = Price


class SizeInline(TabularInline):
    model = Size


class ProductImageInline(TabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', ]
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ColorInline, PriceInline, SizeInline]

    # def save_model(self, request, obj, form, change):
    #     # Combine cat_name and cat_id and update the slug
    #     obj.slug = slugify(f"{obj.name}-{obj.id}")
    #     super().save_model(request, obj, form, change)


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
    list_display = ['id', 'title', 'text']
    list_display_links = ['id', 'title', 'text']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PriceInline, ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin):
    list_display = ['id', 'image']
    list_display_links = ['id', 'image']





@admin.register(Common)
class CommonAdmin(ModelAdmin):
    list_display = ['id', 'facebook', 'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'whatsapp']
    list_display_links = ['id', 'facebook', 'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'whatsapp']
