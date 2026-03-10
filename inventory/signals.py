from django.db.models.signals import post_save
from django.dispatch import receiver

# Import models on which signals will run
from .models import ProductSale, ProductUsage, ProductOrderItem

# Import stock management functions
from .services import increase_stock, decrease_stock


# Signal: Reduce stock when a product is sold
@receiver(post_save, sender=ProductSale)
def reduce_stock_on_sale(sender, instance, created, **kwargs):

    # 'created' ensures this runs only when a new sale is created
    # and not when an existing record is updated
    if created:

        # Decrease stock based on quantity sold
        decrease_stock(instance.product, instance.quantity)


# Signal: Reduce stock when a product is used internally
@receiver(post_save, sender=ProductUsage)
def reduce_stock_on_usage(sender, instance, created, **kwargs):

    # Run only when a new usage record is created
    if created:

        # Decrease stock based on quantity used
        decrease_stock(instance.product, instance.quantity)


# Signal: Increase stock when products are ordered/purchased
@receiver(post_save, sender=ProductOrderItem)
def add_stock_on_purchase(sender, instance, created, **kwargs):

    # Run only when a new order item is created
    if created:

        # Increase stock based on quantity purchased
        increase_stock(instance.product, instance.quantity)
