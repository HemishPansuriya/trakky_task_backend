from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProductSale, ProductUsage, ProductOrderItem
from .services import increase_stock, decrease_stock


@receiver(post_save, sender=ProductSale)
def reduce_stock_on_sale(sender, instance, created, **kwargs):

    if created:
        decrease_stock(instance.product, instance.quantity)


@receiver(post_save, sender=ProductUsage)
def reduce_stock_on_usage(sender, instance, created, **kwargs):

    if created:
        decrease_stock(instance.product, instance.quantity)


@receiver(post_save, sender=ProductOrderItem)
def add_stock_on_purchase(sender, instance, created, **kwargs):

    if created:
        increase_stock(instance.product, instance.quantity)