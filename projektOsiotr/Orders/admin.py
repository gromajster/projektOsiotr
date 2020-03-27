from django.contrib import admin

# Register your models here.
from projektOsiotr.Orders.models import Fish, FishType, Order, OrderItem


@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    pass


@admin.register(FishType)
class FishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
