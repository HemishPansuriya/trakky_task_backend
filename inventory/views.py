from rest_framework import viewsets

# Import all models from models.py
from .models import *

# Import all serializers from serializers.py
from .serializers import *


# Distributor ViewSet
# Provides API endpoints to perform CRUD operations on Distributor
class DistributorViewSet(viewsets.ModelViewSet):

    # Queryset defines which data will be fetched from database
    queryset = Distributor.objects.all()

    # Serializer defines how the data will be converted to/from JSON
    serializer_class = DistributorSerializer


# Product ViewSet
# Handles API operations for Product model
class ProductViewSet(viewsets.ModelViewSet):

    # Fetch all products from database
    queryset = Product.objects.all()

    # Use ProductSerializer to convert data
    serializer_class = ProductSerializer


# Inventory ViewSet
# ReadOnlyModelViewSet means only GET operations are allowed
# (list and retrieve). No create, update, or delete.
class InventoryViewSet(viewsets.ReadOnlyModelViewSet):

    # Fetch all inventory records
    queryset = Inventory.objects.all()

    # Convert inventory data to API response
    serializer_class = InventorySerializer


# ProductOrder ViewSet
# Handles product order creation, update, delete, and retrieval
class ProductOrderViewSet(viewsets.ModelViewSet):

    # Get all product orders
    queryset = ProductOrder.objects.all()

    # Use serializer that supports nested order items
    serializer_class = ProductOrderSerializer


# ProductSale ViewSet
# Handles product sales API
class ProductSaleViewSet(viewsets.ModelViewSet):

    # Get all sales records
    queryset = ProductSale.objects.all()

    # Serializer for product sale
    serializer_class = ProductSaleSerializer


# ProductUsage ViewSet
# Handles internal product usage (example: salon services)
class ProductUsageViewSet(viewsets.ModelViewSet):

    # Get all usage records
    queryset = ProductUsage.objects.all()

    # Serializer for product usage
    serializer_class = ProductUsageSerializer
