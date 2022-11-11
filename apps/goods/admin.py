#管理站点模型的声明文件，默认为空。
from django.contrib import admin
from apps.goods.models import Goods


admin.site.register(Goods)

