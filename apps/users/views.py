import json
import time

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import Users
from apps.users.serializer import CreateUserSerializer


#获取用户信息
def get_userinfo(request):
    user = Users.objects.get(id=1)
    # print(user)
    result = render(request, 'userinfo.html', context={
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    })
    return result

#用户注册
class RegisterView(APIView): #APIView：使用Django rest framework 使代码更简洁，同时方便jwt校验流程
    authentication_classes = () # 不再进行token校验 如果需要排除接口的校验，比如登录接口，只有登录才能获得token，因此在接口类下面加入下面的一行
    def post(self, request):
        import json
        user_data = json.loads(request.body)
        serializer=CreateUserSerializer(data={
            "first_name": user_data.get("first_name"),
            "last_name": user_data.get("last_name"),
            "gender": user_data.get("gender"),
            "email":user_data.get("email"),
            "password": user_data.get("password"),
        })
        if not serializer.is_valid():
            return Response(serializer.errors)
        # create方法
        user = Users.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            gender=user_data['gender'],
            email=user_data['email'],
            password=user_data['password']
        )

        cache.delete('user_data')#旁路模式，删除缓存

        # 创建用户
        return JsonResponse({'code': 200, 'message': 'success', "data": {
            "userId": user.id
        }})

#用户登录
def UserLogin(request):
    if request.method=='POST':
        data = json.loads(request.body)
        email = data.get('email')
        pswd = data.get('password')
        user = Users.objects.filter(email=email).first()
        if not user:
            return JsonResponse({
                'code': 404,
                'message': "User data not exist"
            })
        if user.password!=pswd:
            return JsonResponse({
                'code': 404,
                'message': "User password not correct"
            })
        payload = {
            "email": email,
            # "exp":int(time.time())+30*60,
            "exp": int(time.time()) + 300000 * 60,
        }
        from django.conf import settings
        import jwt
        secret_key = settings.SECRET_KEY
        token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
        return JsonResponse({
            'code': 200,
            'message': 'success',
            'data': {
                'token': token
            }
        })

#用户更改密码
class ChangePasswordView(APIView):
    # authentication_classes = ()
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        pswd = data.get('password')
        npswd = data.get('new-password')
        _user = Users.objects.filter(email=email)
        user=_user.first()
        if not user:
            return JsonResponse({
                'code': 404,
                'message': "User data not exist"
            })
        if user.password!=pswd:
            return JsonResponse({
                'code': 404,
                'message': "User password not correct"
            })
        if pswd==npswd:
            return JsonResponse({
                'code': 404,
                'message': "two password is the same"
            })
        _user.update(password=npswd)
        # Users.objects.filter(email=email).update(password=npswd) #又查一遍很浪费时间
        return JsonResponse({
            'code':200,
            'message': 'success',
            'new-password': npswd
        })

