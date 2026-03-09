from rest_framework import serializers
from .models import *


class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"



class ProductOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrderItem
        fields = ["product", "quantity", "price"]


class ProductOrderSerializer(serializers.ModelSerializer):

    items = ProductOrderItemSerializer(many=True)

    class Meta:
        model = ProductOrder
        fields = ["id", "distributor", "status", "total_amount", "items"]

    def create(self, validated_data):

        items_data = validated_data.pop("items")

        order = ProductOrder.objects.create(**validated_data)

        for item in items_data:
            ProductOrderItem.objects.create(order=order, **item)

        return order
    

class ProductSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSale
        fields = "__all__"

class ProductUsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductUsage
        fields = "__all__"