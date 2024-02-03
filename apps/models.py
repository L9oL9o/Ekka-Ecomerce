from django.db.models import *


class Category(Model):
    name = CharField(max_length=255, verbose_name='Category Name')
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


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


class Price(Model):
    category_id = ForeignKey(Category, CASCADE, related_name='Price')
    color = ForeignKey(Color, on_delete=CASCADE, related_name='Price')
    size = ForeignKey(Size, on_delete=CASCADE, related_name='Price')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    # slug = SlugField(max_length=255, unique=True)
    count = PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.price)


class Product(Model):
    category_id = ForeignKey(Category, CASCADE, related_name='Product')
    name = CharField(max_length=255, verbose_name="Product Name")
    title = CharField(max_length=255, verbose_name="Product Title")
    text = TextField()

    def __str__(self):
        return self.name


class ProductImage(Model):
    product_id = ForeignKey(Product, CASCADE, related_name='ProductImage')
    image = ImageField(upload_to='ProductImages/')
