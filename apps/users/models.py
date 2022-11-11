# 添加模型层数据类的文件。

from enum import IntEnum

from apiview.model import BaseModel
from django.db import models
# Create your models here.

class UserGender(IntEnum):
    FEMALE = 0
    MALE = 1
    LADYBOY = 2

    @classmethod
    def choices(cls):
        return tuple(((item.value, item.name) for item in cls))

class Users(BaseModel):

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200)
    gender = models.SmallIntegerField(choices=UserGender.choices())  # 创建UserGender类
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200,default='123456')# 默认等于123456

    def __str__(self): #将模型类以字符串的方式输出
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'users' # 指明数据库表名
        verbose_name = 'users' # 在admin站点中显示的名称
        verbose_name_plural = 'users' # 在admin站点中显示的名称单复数相同
