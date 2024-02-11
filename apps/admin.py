from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from apps.models import *


class ColorInline(TabularInline):
    model = Color
    # fk_name = 'category'


class PriceInline(TabularInline):
    model = Price
#     fk_name = 'category'  # Specify the ForeignKey name


class SizeInline(TabularInline):
    model = Size
#     fk_name = 'category'


class ProductImageInline(TabularInline):
    model = ProductImage
#     fk_name = 'product'


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ColorInline, PriceInline, SizeInline]
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug', 'get_size_name', "get_price"]
    list_display_links = ['id', 'name', 'slug', 'get_size_name', "get_price"]
    prepopulated_fields = {"slug": ('name',)}
    inlines = [PriceInline, ProductImageInline]
    search_fields = ['name', 'category__title', 'prices__price']
    autocomplete_fields = ["category"]

    def get_size_name(self, obj):
        # Assuming there's a ForeignKey relationship from Price to Size
        if obj.prices.exists():
            # Assuming each product has only one price and each price has a size
            return obj.prices.first().size.name
        return None

    get_size_name.short_description = 'Size Name'

    def get_price(self, obj):
        # Assuming there's a ForeignKey relationship from Product to Price
        if obj.prices.exists():
            # Assuming each product has only one price
            return obj.prices.first().price
        return None

    get_price.short_description = 'Price'


@admin.register(Color)
class ColorAdmin(ModelAdmin):
    list_display = ['id', 'category', 'name', 'slug']
    list_display_links = ['id', 'category', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Price)
class PriceAdmin(ModelAdmin):
    list_display = ['product', 'id', 'category', 'color', 'size', 'price', 'count']
    search_fields = ['size__name', 'color__name', 'product__name']
    list_display_links = ['product', 'id', 'category', 'color', 'size', 'price', 'count']
    list_filter = ['size', 'color', 'price', 'count']
    autocomplete_fields = ['size', 'color', 'product']
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin):
    list_display = ['id', 'product', 'image']
    list_display_links = ['id', 'image']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
