from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product


@receiver(post_save, sender=Product)
def product_post_save(instance, created, **kwargs):
    if instance.discount_id:
        product_price = instance.prices.all()
        discount = instance.discount_id.discount
        for price in product_price:
            price.discount_price = (price.price / 100) * (100 - discount)
            price.save()
