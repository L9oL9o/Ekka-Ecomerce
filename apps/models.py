from django.db.models import Model, DateTimeField, URLField, CharField, IntegerField, SlugField, ForeignKey, TextField, \
    CASCADE, PositiveIntegerField, DecimalField, ImageField, BooleanField


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
    name = CharField(max_length=255, verbose_name='Category Name')
    slug = SlugField(unique=True, verbose_name='Category Slug')

    def __str__(self):
        return self.name


class Color(BaseModel):
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='color')
    name = CharField(max_length=255, verbose_name="Color Name")
    slug = SlugField(max_length=255, unique=False, verbose_name='Color Slug')

    def __str__(self):
        return self.name


class Size(BaseModel):
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='sizes')
    name = CharField(max_length=255, verbose_name="Size Name")
    slug = SlugField(max_length=255, unique=True, verbose_name="Size Slug")

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='products', verbose_name='Product Category')
    name = CharField(max_length=255, verbose_name="Product Title")
    slug = SlugField(max_length=255, unique=True, verbose_name='Product Slug')
    text = TextField(verbose_name="Product Text")
    discount = ForeignKey('apps.Discount', on_delete=CASCADE, related_name='products', verbose_name="Product Discount",
                          null=True, blank=True)

    def __str__(self):
        return self.name


class Price(BaseModel):
    product = ForeignKey("apps.Product", on_delete=CASCADE, related_name='prices', verbose_name="Price Product")
    category = ForeignKey("apps.Category", on_delete=CASCADE, related_name='prices', verbose_name="Price Category")
    color = ForeignKey("apps.Color", on_delete=CASCADE, related_name='prices', verbose_name="Price Color")
    size = ForeignKey("apps.Size", on_delete=CASCADE, related_name='prices', verbose_name="Price Size")
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name="prices")
    count = PositiveIntegerField(default=0, verbose_name="Price Count")

    def __str__(self):
        return f"{self.product.name} {self.size.name} {self.color.name}"

    # def __str__(self):
    #     return [self.product.name, self.size.name, self.color.name, ]


class Discount(BaseModel):
    name = CharField(max_length=255, verbose_name="Discount Name")
    percentage = PositiveIntegerField(default=0, verbose_name="Discount Percentage")

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = ForeignKey("apps.Product", on_delete=CASCADE, related_name='images', verbose_name='Product Product')
    price = ForeignKey("apps.Price", on_delete=CASCADE, related_name='images', verbose_name='Product Price')
    image = ImageField(upload_to='product_images/', verbose_name='Product Image')

    def __str__(self):
        return self.product.name

#
# class BaseModel(Model):
#     created_time = DateTimeField(auto_now_add=True)
#     updated_time = DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.created_time)
#
#
# class Common(BaseModel):
#     facebook = URLField(verbose_name="Facebook")
#     twitter = URLField(verbose_name="Twitter")
#     instagram = URLField(verbose_name="Instagram")
#     linkedin = URLField(verbose_name="LinkedIN")
#     youtube = URLField(verbose_name="Youtube")
#     whatsapp = URLField(verbose_name="Whatsapp")
#
#
# class Category(BaseModel):
#     name = CharField(max_length=255, verbose_name='Category Name')
#     slug = SlugField(unique=True, verbose_name='Slug')
#
#     def __str__(self):
#         return self.name
#
#
# class Color(BaseModel):
#     category_id = ForeignKey(Category, CASCADE, related_name='Color')
#     name = CharField(max_length=255, verbose_name="Color Name")
#     slug = SlugField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Size(BaseModel):
#     category_id = ForeignKey(Category, CASCADE, related_name='Size')
#     name = CharField(max_length=255, verbose_name="Size Name")
#     slug = SlugField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(BaseModel):
#     category = ForeignKey(Category, CASCADE, related_name='products')
#     name = CharField(max_length=255, verbose_name="Product Title")
#     slug = SlugField(max_length=255, unique=True)
#     text = TextField(verbose_name="Product Text")
#
#     def __str__(self):
#         return self.name
#
#

#
# class ProductImage(BaseModel):
#     product_id = ForeignKey(Product, CASCADE, related_name='ProductImage', verbose_name='Product Category ID')
#     product_price = ForeignKey("apps.Price", on_delete=CASCADE)
#     image = ImageField(upload_to='ProductImages/', verbose_name='Product Image')
#
#
#
# # class Product(Model):
# #     category_id = ForeignKey(Category, CASCADE, related_name='Product')
# #     name = CharField(max_length=255, verbose_name="Product Name")
# #     title = CharField(max_length=255, verbose_name="Product Title")
# #     text = TextField(verbose_name="Product Text")
# #     avatar_img = ImageField(upload_to='Product_main_image/%Y/%m/%d', verbose_name="Product Main Image", null=True, blank=True)
# #
# #     def __str__(self):
# #         return self.name
