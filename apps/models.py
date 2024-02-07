from autoslug import AutoSlugField
from django.db.models import *
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class BaseModel(Model):
    created_time = DateTimeField(auto_now_add=True)
    updated_time = DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_time

    # class Meta:
    #     abstract = True


class Common(BaseModel):
    facebook = URLField(verbose_name="Facebook")
    twitter = URLField(verbose_name="Twitter")
    instagram = URLField(verbose_name="Instagram")
    linkedin = URLField(verbose_name="LinkedIN")
    youtube = URLField(verbose_name="Youtube")
    whatsapp = URLField(verbose_name="Whatsapp")


class Category(Model):
    name = CharField(max_length=255, verbose_name='Category Name')
    slug = SlugField(unique=True, verbose_name='Slug')

    # slug = AutoSlugField(populate_from='name', unique=True , always_update=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.name:
    #         self.slug = slugify(self.name) + '-' + str(self.id)
    #     super(Category, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # Combine category_name and category_id to create a unique slug
    #     slug = f"{slugify(self.name)}-{self.id}"
    #
    #     # You may want to check if this slug already exists and handle it accordingly
    #
    #     self.slug = slug
    #     super(Category, self).save(*args, **kwargs)
    #
    #     # Update the slug field with the actual ID after saving
    #     self.slug = f"{slug}-{self.id}"
    #     self.save(update_fields=['slug'])


class Color(Model):
    category_id = ForeignKey(Category, CASCADE, related_name='Color')
    name = CharField(max_length=255, verbose_name="Color Name")
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Size(Model):
    category_id = ForeignKey(Category, CASCADE, related_name='Size')
    name = CharField(max_length=255, verbose_name="Size Name")
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(Model):
    category = ForeignKey(Category, CASCADE, related_name='products')
    title = CharField(max_length=255, verbose_name="Product Title")
    slug = SlugField(max_length=255, unique=True)
    text = TextField(verbose_name="Product Text")

    def __str__(self):
        return self.title


class Price(Model):
    product = ForeignKey("apps.Product", CASCADE, related_name='price')
    category = ForeignKey("apps.Category", CASCADE, related_name='price')
    color = ForeignKey(Color, CASCADE, related_name='price')
    size = ForeignKey(Size, CASCADE, related_name='price')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    count = PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.title} {self.size.name} {self.color.name}"

# class Product(Model):
#     category_id = ForeignKey(Category, CASCADE, related_name='Product')
#     name = CharField(max_length=255, verbose_name="Product Name")
#     title = CharField(max_length=255, verbose_name="Product Title")
#     text = TextField(verbose_name="Product Text")
#     avatar_img = ImageField(upload_to='Product_main_image/%Y/%m/%d', verbose_name="Product Main Image", null=True, blank=True)
#
#     def __str__(self):
#         return self.name


class ProductImage(Model):
    product_id = ForeignKey(Product, CASCADE, related_name='ProductImage', verbose_name='Product Category ID')
    product_price = ForeignKey("apps.Price", on_delete=CASCADE)
    image = ImageField(upload_to='ProductImages/', verbose_name='Product Image')


