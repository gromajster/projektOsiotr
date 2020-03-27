from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from projektOsiotr.Orders.models import Fish, FishType, OrderItem, Order
from projektOsiotr.Orders.serializers import FishSerializer, FishTypeSerializer, OrderItemSerializer, OrderSerializer, \
    SaveOrderSerializer


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    http_method_names = ['get', 'post']


class FishTypeViewSet(viewsets.ModelViewSet):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
    http_method_names = ['get', 'post']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SaveOrderSerializer
        return super().get_serializer_class()


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ['get', 'post']
