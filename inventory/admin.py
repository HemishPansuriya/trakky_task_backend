from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Distributor)
admin.site.register(ProductOrder)
admin.site.register(ProductOrderItem)
admin.site.register(ProductSale)
admin.site.register(ProductUsage)
admin.site.register(Inventory)
admin.site.register(InUseInventory)
admin.site.register(InventoryTransaction)