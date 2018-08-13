from django.db import models


# Create your models here.
class Announcement(models.Model):
    title = models.CharField('Announcement title', max_length=200)
    description = models.TextField('Announcement description', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class Restaurant(models.Model):
    name = models.CharField('Restaurant name', max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="items", on_delete=models.CASCADE)
    name = models.CharField('Item name', max_length=200)
    price = models.FloatField('Price', default=0.0)

    def __str__(self):
        return self.name


class Order(models.Model):
    date_placed = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, related_name="orders", on_delete=models.CASCADE)
    # items = models.ManyToManyField(MenuItem, through="OrderedItem")


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity')