from rest_framework import serializers
from .models import *


# Distributor Serializer
# Converts Distributor model data to JSON and JSON to model instance
class DistributorSerializer(serializers.ModelSerializer):

    class Meta:
        # Model that will be serialized
        model = Distributor

        # "__all__" means include all fields of the model
        fields = "__all__"


# Product Serializer
# Used to convert Product model data to API response and accept API request data
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


# Inventory Serializer
# Used to expose inventory data through API
class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = "__all__"



# ProductOrderItem Serializer
# This serializer handles each product inside an order
class ProductOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        # Model used for order items
        model = ProductOrderItem

        # Only these fields will be included in API
        fields = ["product", "quantity", "price"]


# ProductOrder Serializer
# Handles the complete order including multiple items
class ProductOrderSerializer(serializers.ModelSerializer):

    # Nested serializer
    # This allows sending multiple products in a single order
    items = ProductOrderItemSerializer(many=True)

    class Meta:
        model = ProductOrder

        # Fields exposed in API
        fields = ["id", "distributor", "status", "total_amount", "items"]

    # Custom create method
    # This is required because we are using nested serializer (items)
    def create(self, validated_data):

        # Remove items from main validated data
        items_data = validated_data.pop("items")

        # Create the main order
        order = ProductOrder.objects.create(**validated_data)

        # Loop through each item and create ProductOrderItem
        for item in items_data:
            ProductOrderItem.objects.create(order=order, **item)

        # Return created order
        return order
    

# ProductSale Serializer
# Used when products are sold to customers
class ProductSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSale
        fields = "__all__"


# ProductUsage Serializer
# Used when products are used internally (example: salon service use)
class ProductUsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductUsage
        fields = "__all__"
