from django.db import models
from django.db.models import SET_NULL


class FishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fish(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(FishType, on_delete=SET_NULL, null=True)
    latin_name = models.CharField(max_length=100)
    size = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    picture = models.FileField()
    description = models.TextField(default="Opis", max_length=1000)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    company_name = models.CharField(max_length=30)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    fishes = models.ManyToManyField(Fish, through='OrderItem')
    cost = models.DecimalField(max_digits=8, decimal_places=2) 

    def __str__(self):
        return "Zamówienie firmy " + self.company_name


class OrderItem(models.Model):
    fish = models.ForeignKey(Fish, on_delete=SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=SET_NULL, null=True, related_name='items')
    amount = models.IntegerField()



