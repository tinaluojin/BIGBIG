"""shopping_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.carts.views import AddCartsView, EditCartsView
from apps.goods.views import GoodsView
from apps.orders.views import MakeOrderView, GetOrdersView
from apps.users.views import get_userinfo, RegisterView, ChangePasswordView, UserLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinfo', get_userinfo),
    path('api/users/register', RegisterView.as_view()),
    path('api/users/login', UserLogin),
    path('api/users/change-password',ChangePasswordView.as_view()),
    path('api/goods/get-goods',GoodsView.as_view()),
    path('api/carts/add-carts',AddCartsView.as_view()),
    path('api/carts/edit-carts',EditCartsView.as_view()),
    path('api/orders/make-order',MakeOrderView.as_view()),
    path('api/orders/get-orders',GetOrdersView.as_view())
]
