import random
import string

import webcolors
from colorfield.fields import ColorField
from slugify import slugify
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db.models import Model, DateTimeField, URLField, CharField, IntegerField, SlugField, ForeignKey, TextField, \
    CASCADE, PositiveIntegerField, DecimalField, ImageField, BooleanField, ManyToManyField


class BaseModel(Model):
    created_time = DateTimeField(auto_now_add=True)
    updated_time = DateTimeField(auto_now=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.is_active

    class Meta:
        abstract = True


class Common(BaseModel):
    facebook = URLField(verbose_name="Facebook")
    twitter = URLField(verbose_name="Twitter")
    instagram = URLField(verbose_name="Instagram")
    linkedin = URLField(verbose_name="LinkedIN")
    youtube = URLField(verbose_name="Youtube")
    whatsapp = URLField(verbose_name="Whatsapp")

    def __str__(self):
        return [self.facebook, self.twitter, self.instagram, self.linkedin, self.youtube, self.whatsapp]


class Category(BaseModel):
    name = CharField(max_length=255, verbose_name=_('Name'))
    slug = SlugField(unique=True, verbose_name='Slug')

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

    def __str__(self):
        return self.name


class Color(BaseModel):
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='color')
    name = CharField(max_length=255, verbose_name=" Name")
    color_choice = ColorField(default='#FF0000', format="hexa", verbose_name="Color")
    slug = SlugField(max_length=255, unique=False, verbose_name='Slug')

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(20)])
        random_int = random.randint(10000, 9999999)
        done_slug = "-".join(str(random_int)) + "/" + "-".join(slug) + "/" + "-".join(random_data)
        return done_slug

    def save(self, *args, **kwargs):
        if self.name is None:
            self.slug = slugify(self.color_choice)
        else:
            self.slug = slugify(self.name)
        self.slug = self.__generate_slug(self.slug)
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Size(BaseModel):
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='sizes')
    name = CharField(max_length=255, verbose_name="Name")
    slug = SlugField(max_length=255, unique=True, verbose_name="Slug")

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

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='products', verbose_name='Category')
    name = CharField(max_length=255, verbose_name="Title")
    slug = SlugField(max_length=255, unique=True, verbose_name='Slug')
    text = TextField(verbose_name="Text")
    discount_id = ForeignKey('apps.Discount', on_delete=CASCADE, related_name='products', verbose_name="Discount",
                             null=True, blank=True)

    currency_ids = ManyToManyField('apps.Currency', related_name='products')

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

    def __str__(self):
        return self.name

    # HERE GPT SUGGESTED TO GET DISCOUNT PRICE
    # def get_discounted_price(self):
    #     # Check if the product has a discount associated with it
    #     if self.discount:
    #         # Calculate the discounted price based on the discount percentage
    #         discounted_price = (self.price / 100) * (100 - self.discount.discount)
    #         return discounted_price
    #     else:
    #         # If there is no discount, return the regular price
    #         return self.price


class Price(BaseModel):
    product = ForeignKey("apps.Product", on_delete=CASCADE, related_name='prices', verbose_name="Product")
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='prices', verbose_name="Category")
    color = ForeignKey("apps.Color", on_delete=CASCADE, related_name='prices', verbose_name="Color")
    size = ForeignKey("apps.Size", on_delete=CASCADE, related_name='prices', verbose_name="Size")
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    count = PositiveIntegerField(default=0, verbose_name="  Count")

    def __str__(self):
        return f"{self.product.name} {self.size.name} {self.color.name}"


class Discount(BaseModel):
    name = CharField(max_length=255, verbose_name=" Name")
    slug = SlugField(max_length=255, verbose_name="Slug")
    text = TextField(max_length=255, verbose_name="Text")
    percentage = PositiveIntegerField(default=0, verbose_name="Percentage")
    count = PositiveIntegerField(default=10, verbose_name="Count")

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

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = ForeignKey("apps.Product", on_delete=CASCADE, related_name='images', verbose_name='Product')
    price = ForeignKey("apps.Price", on_delete=CASCADE, related_name='images', verbose_name='Price')
    image = ImageField(upload_to='product_images/', verbose_name='Image')

    def __str__(self):
        return self.product.name


class Currency(BaseModel):
    name = CharField(max_length=255, verbose_name="Name of Currency")
    slug = SlugField(max_length=255, unique=True, verbose_name="Slug")
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

    def __str__(self):
        return self.name
