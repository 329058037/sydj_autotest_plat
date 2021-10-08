from django.contrib import admin
from apitest.models import Apis, Apistep, Apitest
from product.models import Product
# Register your models here.

class ApistepAdmin(admin.TabularInline):
    list_display = [
        'apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id', 'product'
    ]
    model = Apistep
    extra = 1
    admin.site.register(Apis)



class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]


admin.site.register(Apitest, ApitestAdmin)