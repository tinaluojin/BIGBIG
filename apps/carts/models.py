from django.db import models
# Create your models here.
# 添加模型层数据类的文件。

from django.db import models

# Create your models here.
from apps.utils.base_model import BaseModel
from apps.users.models import Users
from apps.goods.models import Goods

#建立一个中间表，由于一个用户对应一个购物车，因此不需要建立购物车表，同时用户与商品构成m:n的关系，因此建立中间表存储添加购物车这个过程

class CartsGoods(BaseModel):
    user = models.ForeignKey(Users, related_name='user_cartsGoods', on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, related_name='good_cartsGoods', on_delete=models.CASCADE)
    num = models.IntegerField(default=0) # 整数字段，默认等于0
    class Meta:
        db_table = 'cartsGoods' # 指明数据库表名
        verbose_name = 'cartsGoods' # 在admin站点中显示的名称
        verbose_name_plural = 'cartsGoods'  # 在admin站点中显示的名称单复数相同

    # django中related_name的作用和用法
    # 其实可以就理解为, 一对多关系拿对象的解决。可以把引用理解为主从关系
    # 主引用从, 即一对多, 注意外键字段是放在多的一端的,
    # 比如一个班级class 有很多同学students, 那么就在students类里面设置class字段值是外键类型
    # 从students拿class数据很好拿, studets.class就拿到了
    # 但是从class 拿students数据就不好拿了, 当然也可以拿, 默认的方式是class.students_set.all()也可以拿到
    # 不过这样麻烦, 简单一点就是设置一个related_name = classs属性直接class .classs.all() 就可以了

    # update 是主键表中被参考字段的值更新；delete是指在主键表中删除一条记录
    # on_update 和 on_delete 后面可以跟的词语：

    # on_delete = None,  # 删除关联表中的数据时,当前表与其关联的field的行为
    # on_delete = models.CASCADE,  # 删除关联数据,与之关联也删除
    # on_delete = models.DO_NOTHING,  # 删除关联数据,什么也不做
    # on_delete = models.PROTECT,  # 删除关联数据,引发错误ProtectedError
    # on_delete = models.SET,  # 删除关联数据,

    # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete = models.SET_NULL,  # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）

    # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    # on_delete = models.SET_DEFAULT,  # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）


