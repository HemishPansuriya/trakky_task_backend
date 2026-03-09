from rest_framework import viewsets

from .models import *
from .serializers import *


class DistributorViewSet(viewsets.ModelViewSet):

    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InventoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ProductOrderViewSet(viewsets.ModelViewSet):

    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer


class ProductSaleViewSet(viewsets.ModelViewSet):

    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer


class ProductUsageViewSet(viewsets.ModelViewSet):

    queryset = ProductUsage.objects.all()
    serializer_class = ProductUsageSerializer