from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
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
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['slug',]
    inlines = [ColorInline, PriceInline, SizeInline]
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['id', 'name',    'get_size_name', "get_price"]
    list_display_links = ['id', 'name',  'get_size_name', "get_price"]
    # prepopulated_fields = {"slug": ('name',)}
    readonly_fields = ["slug",]
    inlines = [PriceInline, ProductImageInline]
    search_fields = ['name', 'category__name', 'price__price']
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

    # HERE GPT SUGGESTED TO GET DISCOUNT PRICE
    # def get_discounted_price(self, obj):
    #     return obj.get_discounted_price()
    #
    # get_discounted_price.short_description = 'Discounted Price'


@admin.register(Color)
class ColorAdmin(ModelAdmin):
    list_display = ['id', 'category', "name", "color_choice"]
    list_display_links = ['id', 'category', "name", "color_choice"]
    prepopulated_fields = {'name': ('color_choice',)}
    search_fields = ['name']
    readonly_fields = ["slug",]

    def display_color(self, obj):
        return '<div style="width: 30px; height: 30px; background-color: {};"></div>'.format(obj.color)

    display_color.allow_tags = True
    display_color.short_description = 'Color'


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["slug",]
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


@admin.register(Currency)
class CurrencyAdmin(ModelAdmin):
    list_display = ['id', "name", 'rate']
    list_display_links = ['id', "name", 'rate']
    readonly_fields = ["slug",]


@admin.register(Discount)
class CurrencyAdmin(ModelAdmin):
    list_display = ['id', "name", 'text', "percentage", "count"]
    list_display_links = ['id', "name", 'text', "percentage", "count"]
    readonly_fields = ["slug",]