from django.contrib import admin
from bug.models import Bug
# Register your models here.


class BugAdmin(admin.ModelAdmin):
    list_display = [
        'bugname', 'bugdetail', 'bugstatus', 'buglevel', 'bugcreater', 'bugassign', 'create_time', 'id'
    ]
    # 把BUG管理模块注册到Django admin 后台并能显示
    admin.site.register(Bug)
