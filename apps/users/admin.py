from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from apps.users.models import Users

admin.site.unregister(User) #注册（register）或删除（unregistered）后台管理界面的模型
admin.site.unregister(Group)

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'gender']
    # Users.name.short_description ='姓名' # 用于显示时的名字 , 没有这个,字段标题将显示'name'
    # list_display = ['account','name','password'] #显示的字段
    # list_per_page = 5  #设置每页显示记录
    # ordering = ('-id',)  #设置排序负数标识降序
    # list_editable = ['name']  #设置可编辑字段
    # list_display_links = ('account','password')  #设置哪些字段点击链接可进入编辑界面
    # list_filter = ('account','name')  #过滤器
    # search_fields = ('acccount','name')  #搜索字段
    # date_hierarchy = 'gotime'  #详细时间筛选