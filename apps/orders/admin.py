from django.contrib import admin

from apps.orders.models import Orders, OrdersGoods

admin.site.register(Orders)
admin.site.register(OrdersGoods)