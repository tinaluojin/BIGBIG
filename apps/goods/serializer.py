
# 序列化，没规则转为有规则。当用户需要查询数据的时候，把数据库里面的数据转成我们需要的json数据，这个过程就是序列化
from rest_framework import serializers
from apps.goods.models import Goods

class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__' #返回全部字段
        # fields = ['id','first_name']
        # exclude = ['id']