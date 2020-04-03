from rest_framework import viewsets, permissions

from projektOsiotr.orders.models import Fish, FishType, OrderItem, Order
from projektOsiotr.orders.serializers import FishSerializer, FishTypeSerializer, OrderItemSerializer, OrderSerializer, \
    SaveOrderSerializer


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    http_method_names = ['get', 'post']

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAdminUser, ]
        return super(FishViewSet, self).get_permissions()


class FishTypeViewSet(viewsets.ModelViewSet):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
    http_method_names = ['get', 'post']

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAdminUser, ]
        return super(FishTypeViewSet, self).get_permissions()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SaveOrderSerializer
        return super().get_serializer_class()


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = OrderItemSerializer
    http_method_names = ['get', 'post']
