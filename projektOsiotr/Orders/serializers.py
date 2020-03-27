from idlelib import query

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField, PrimaryKeyRelatedField

from projektOsiotr.Orders.models import Fish, FishType, OrderItem, Order


class FishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishType
        fields = ['id', 'name']


class FishSerializer(serializers.ModelSerializer):
    type = StringRelatedField(many=False)

    class Meta:
        model = Fish
        fields = ['id', 'name', 'type', 'latin_name', 'size', 'price', 'description', 'stock']


class OrderFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ['name', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    fish = OrderFishSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['fish', 'amount']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'company_name', 'name', 'surname', 'date_created', 'status', 'cost', 'items']


class OrderItemSaveSerializer(serializers.ModelSerializer):
    fish = serializers.PrimaryKeyRelatedField(queryset=Fish.objects.all())

    class Meta:
        model = OrderItem
        fields = ['fish', 'amount']


class SaveOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSaveSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'company_name', 'name', 'surname', 'date_created', 'status', 'cost', 'items']

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        fishes = Fish.objects.all()
        for item in items:
            item['order'] = order

        OrderItem.objects.bulk_create(OrderItem(**item) for item in items)
        return order
