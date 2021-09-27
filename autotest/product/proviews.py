from django.shortcuts import render
from product.models import product

# Create your views here.

# 产品管理

def product_manage(request):
    username = request.session.get('user', '')
    product_list = product.objects.all()
    return render(request, "product_manage.html", {"user": username, "products": product_list})
    

def mytemplate(request):
    return render(request, 'mytemplate.html')