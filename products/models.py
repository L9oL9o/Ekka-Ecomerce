import random
import string
from common.models import BaseModel
from colorfield.fields import ColorField
from slugify import slugify
from django.utils.translation import gettext_lazy as _
from django.db.models import Model, CharField, SlugField, ForeignKey, TextField, CASCADE, PositiveIntegerField, \
    DecimalField, ImageField, ManyToManyField


class Catalog(BaseModel):
    name = CharField(max_length=255, verbose_name=_('Name'))
    slug = CharField(unique=True, max_length=255, verbose_name=_('Slug'))

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_letters
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Catalog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Catalog"

    def __str__(self):
        return f"{self.name}  "


class Category(BaseModel):
    catalog_id = ForeignKey("products.Catalog", verbose_name=_('Catalog'), on_delete=CASCADE, related_name='categories')
    name = CharField(max_length=255, verbose_name=_('Category Name'))
    slug = SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Color(BaseModel):
    category = ForeignKey("products.Category", on_delete=CASCADE, related_name='color')
    name = CharField(max_length=255, verbose_name=_("Name"))
    color_choice = ColorField(verbose_name=_("Color"))
    slug = SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.color_choice)
        self.slug = self.__generate_slug(self.slug)
        super(Color, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Color"

    def __str__(self):
        return self.name


class Size(BaseModel):
    category = ForeignKey("products.Category", on_delete=CASCADE, related_name='sizes')
    name = CharField(max_length=255, verbose_name=_("Name"))
    slug = SlugField(max_length=255, unique=True, verbose_name=_("Slug"))

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Size, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Size"

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = ForeignKey("products.Category", on_delete=CASCADE, related_name='products', verbose_name=_('Category'))
    name = CharField(max_length=255, verbose_name=_("Title"))
    slug = SlugField(max_length=255, unique=True, verbose_name=_('Slug'))
    text = TextField(verbose_name=_("Text"))
    discount_id = ForeignKey('products.Discount', on_delete=CASCADE, related_name='products',
                             verbose_name=_("Discount"),
                             null=True, blank=True)

    currency_ids = ManyToManyField('products.Currency', related_name='products')

    # def clean(self):
    #     if len(self.text) < 50:
    #         raise ValidationError(_("Text 50 ta belgidan kam bo'lmasligi kerak !"))
    #     if str(self.text).isdigit() is False:
    #         raise

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name


class Price(BaseModel):
    product = ForeignKey("products.Product", on_delete=CASCADE, related_name='prices', verbose_name=_("Product"))
    category = ForeignKey("products.Category", on_delete=CASCADE, related_name='prices', verbose_name=_("Category"))
    color = ForeignKey("products.Color", on_delete=CASCADE, related_name='prices', verbose_name=_("Color"))
    size = ForeignKey("products.Size", on_delete=CASCADE, related_name='prices', verbose_name=_("Size"))
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    count = PositiveIntegerField(default=0, verbose_name=_("  Count"))

    class Meta:
        verbose_name_plural = "Price"

    def __str__(self):
        return f"{self.product.name} {self.size.name} {self.color.name}"


class Discount(BaseModel):
    name = CharField(max_length=255, verbose_name=_(" Name"))
    slug = SlugField(max_length=255, verbose_name=_("Slug"))
    text = TextField(max_length=255, verbose_name=_("Text"))
    percentage = PositiveIntegerField(default=0, verbose_name=_("Percentage"))
    count = PositiveIntegerField(default=10, verbose_name=_("Count"))

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Discount, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Discount"

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = ForeignKey("products.Product", on_delete=CASCADE, related_name='images', verbose_name=_('Product'))
    price = ForeignKey("products.Price", on_delete=CASCADE, related_name='images', verbose_name=_('Price'))
    image = ImageField(upload_to='product_images/', verbose_name=_('Image'))

    class Meta:
        verbose_name_plural = "Product Image"

    def __str__(self):
        return self.product.name


class Currency(BaseModel):
    name = CharField(max_length=255, verbose_name=_("Currency Name"))
    slug = SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    rate = DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Currency, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Currency"

    def __str__(self):
        return self.name
