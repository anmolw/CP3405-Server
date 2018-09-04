from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import ValidationError


def restaurant_image_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"res_{instance.id}.{extension}"


# Create your models here.
class Announcement(models.Model):
    title = models.CharField('Announcement title', max_length=200)
    description = models.TextField('Announcement description', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    name = models.CharField('Restaurant name', max_length=200)
    thumbnail = models.ImageField('Restaurant thumbnail', upload_to=restaurant_image_path, default="default.png")

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
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    # items = models.ManyToManyField(MenuItem, through="OrderedItem")


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity')


class Table(models.Model):
    ac = models.BooleanField(name="AC")

    def __str__(self):
        return f"Table #{self.id}: {'AC' if self.AC else 'Non-AC'}"

    def add_reservation(self, reservation):
        if self.reservation_set.count() < 4:
            self.reservation_set.add(reservation)
        else:
            raise ValidationError('Max 4 reservations allowed')


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_placed = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="reservations", on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation #{self.id}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)