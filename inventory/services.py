from .models import Inventory


def increase_stock(product, quantity):

    inventory, created = Inventory.objects.get_or_create(product=product)

    inventory.quantity_available += quantity
    inventory.save()


def decrease_stock(product, quantity):

    inventory, created = Inventory.objects.get_or_create(product=product)

    if inventory.quantity_available < quantity:
        raise Exception("Not enough stock")

    inventory.quantity_available -= quantity
    inventory.save()