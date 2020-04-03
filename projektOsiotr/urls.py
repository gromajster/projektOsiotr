from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projektOsiotr.orders.views import FishViewSet, FishTypeViewSet, OrderItemViewSet, OrderViewSet

router = routers.DefaultRouter()

router.register(r'fish', FishViewSet)
router.register(r'fish_type', FishTypeViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order_item', OrderItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include('projektOsiotr.accounts.urls')),
]
