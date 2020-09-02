from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('1111')
    return HttpResponse('test')

def user_logiin(request):
    print('用户登录成功')
    return HttpResponse('跳转到项目首页')
