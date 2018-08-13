from django.contrib import admin
from api.models import Restaurant, Order, OrderedItem, MenuItem

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
