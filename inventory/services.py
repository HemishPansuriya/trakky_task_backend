from .models import Inventory


# Function to increase stock when products are purchased or added
def increase_stock(product, quantity):

    # Get the inventory record for the product
    # If it does not exist, create a new inventory record
    inventory, created = Inventory.objects.get_or_create(product=product)

    # Add the purchased quantity to the current available stock
    inventory.quantity_available += quantity

    # Save the updated inventory quantity to the database
    inventory.save()


# Function to decrease stock when product is sold or used
def decrease_stock(product, quantity):

    # Get the inventory record for the product
    # If it does not exist, create a new inventory record
    inventory, created = Inventory.objects.get_or_create(product=product)

    # Check if enough stock is available
    if inventory.quantity_available < quantity:
        # Raise an error if stock is not sufficient
        raise Exception("Not enough stock")

    # Reduce the quantity from available stock
    inventory.quantity_available -= quantity

    # Save the updated inventory quantity
    inventory.save()
