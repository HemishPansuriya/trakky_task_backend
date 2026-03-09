from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("products", ProductViewSet)
router.register("distributors", DistributorViewSet)
router.register("orders", ProductOrderViewSet)
router.register("inventory", InventoryViewSet)
router.register("sales", ProductSaleViewSet)
router.register("usage", ProductUsageViewSet)

urlpatterns = router.urls