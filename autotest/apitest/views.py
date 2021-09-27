


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2021/09/24 09:57:54
@Author  :   Wei Kang 
@Version :   1.0
@Contact :   329058037@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   创建登录函数
'''

# here put the import lib
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render
# 加入引用
from django.http import HttpResponse
# Create your views here.
def test(request):
    # 返回 HttpResponse 响应函数
    return HttpResponse("hello test")

def login(request):
    # 返回 HttpResponse 响应函数
    return render(request,'login.html')

def home(request):
    # 返回 HttpResponse 响应函数
    return render(request,'home.html')   

def logout(request):
    auth.logout(request)
    # 返回 HttpResponse 响应函数
    return render(request,'login.html')   

def login(request):

    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)

        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error':'username or password error'})
#    else:
#        context = {}
#        return render(request, 'login.html', context)

    return render(request, 'login.html')
