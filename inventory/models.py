from django.db import models


# Distributor Model
# This model stores information about the product distributors/suppliers
class Distributor(models.Model):

    # Name of the distributor
    name = models.CharField(max_length=200)

    # Phone number of the distributor
    phone = models.CharField(max_length=20)

    # Email address (optional)
    email = models.EmailField(blank=True)

    # Address of the distributor (optional)
    address = models.TextField(blank=True)

    # This method defines how the object will appear in the admin panel or shell
    def __str__(self):
        return self.name


# Product Model
# This model stores all product information
class Product(models.Model):

    # Product type choices
    # SALE = product only for selling
    # USE = product only for internal use (like salon use)
    # BOTH = product can be sold and used
    PRODUCT_TYPE = (
        ("SALE", "Sale"),
        ("USE", "Use"),
        ("BOTH", "Both")
    )

    # Product name
    name = models.CharField(max_length=200)

    # Brand name (optional)
    brand = models.CharField(max_length=200, blank=True)

    # Unique product SKU (Stock Keeping Unit)
    sku = models.CharField(max_length=100, unique=True)

    # Product type (Sale / Use / Both)
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE)

    # Cost price (purchase price)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Selling price (customer price)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Unit of the product (ml, gm, piece, bottle etc.)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Inventory Model
# This model keeps track of available stock of each product
class Inventory(models.Model):

    # One product will have only one inventory record
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    # Total quantity available in stock
    quantity_available = models.FloatField(default=0)

    # Automatically updated when stock changes
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity_available}"
    

# Product Order Model
# Used when ordering products from a distributor
class ProductOrder(models.Model):

    # Order status choices
    STATUS = (
        ("PENDING", "Pending"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    )

    # Distributor from whom the order is placed
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)

    # Order date automatically set
    order_date = models.DateField(auto_now_add=True)

    # Current order status
    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")

    # Total amount of the order
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)


# Product Order Item Model
# Stores individual products inside an order
class ProductOrderItem(models.Model):

    # Reference to the main order
    order = models.ForeignKey(ProductOrder, related_name="items", on_delete=models.CASCADE)

    # Product ordered
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Quantity ordered
    quantity = models.IntegerField()

    # Price of the product during purchase
    price = models.DecimalField(max_digits=10, decimal_places=2)


# Product Sale Model
# Tracks products sold to customers
class ProductSale(models.Model):

    # Product sold
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Quantity sold
    quantity = models.FloatField()

    # Price per unit
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Total price = quantity × price
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    # Time when the product was sold
    sold_at = models.DateTimeField(auto_now_add=True)


# Product Usage Model
# Tracks products used internally (like in salon services)
class ProductUsage(models.Model):

    # Product used
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Quantity used
    quantity = models.FloatField()

    # Used for which purpose/service
    used_for = models.CharField(max_length=255)

    # Time when the product was used
    used_at = models.DateTimeField(auto_now_add=True)


# InUseInventory Model
# Tracks products that are opened and currently being used
class InUseInventory(models.Model):

    # Product reference
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Quantity when the product was opened
    opened_quantity = models.FloatField()

    # Remaining quantity in the opened product
    remaining_quantity = models.FloatField()

    # Date when product was opened
    opened_at = models.DateTimeField(auto_now_add=True)

    # Indicates whether the opened product is still active
    active = models.BooleanField(default=True)


# Inventory Transaction Model
# Keeps a history/log of all inventory movements
class InventoryTransaction(models.Model):

    # Transaction type choices
    TYPE = (
        ("PURCHASE", "Purchase"),  # When product is purchased from distributor
        ("SALE", "Sale"),          # When product is sold
        ("USAGE", "Usage")         # When product is used internally
    )

    # Product involved in the transaction
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Quantity involved in the transaction
    quantity = models.FloatField()

    # Type of transaction
    transaction_type = models.CharField(max_length=20, choices=TYPE)

    # Timestamp of the transaction
    created_at = models.DateTimeField(auto_now_add=True)
