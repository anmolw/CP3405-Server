from django.contrib import admin
from api.models import Restaurant, Order, OrderedItem, MenuItem, Announcement, Table, Reservation, Order

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Announcement)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Reservation)