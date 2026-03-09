from django.db import models


class Distributor(models.Model):

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    PRODUCT_TYPE = (
        ("SALE", "Sale"),
        ("USE", "Use"),
        ("BOTH", "Both")
    )

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True)
    sku = models.CharField(max_length=100, unique=True)

    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE)

    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Inventory(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    quantity_available = models.FloatField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity_available}"
    
class ProductOrder(models.Model):

    STATUS = (
        ("PENDING", "Pending"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    )

    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)

    order_date = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")

    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class ProductOrderItem(models.Model):

    order = models.ForeignKey(ProductOrder, related_name="items", on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductSale(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.FloatField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    sold_at = models.DateTimeField(auto_now_add=True)

class ProductUsage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.FloatField()

    used_for = models.CharField(max_length=255)

    used_at = models.DateTimeField(auto_now_add=True)

class InUseInventory(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    opened_quantity = models.FloatField()

    remaining_quantity = models.FloatField()

    opened_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

class InventoryTransaction(models.Model):

    TYPE = (
        ("PURCHASE", "Purchase"),
        ("SALE", "Sale"),
        ("USAGE", "Usage")
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.FloatField()

    transaction_type = models.CharField(max_length=20, choices=TYPE)

    created_at = models.DateTimeField(auto_now_add=True)