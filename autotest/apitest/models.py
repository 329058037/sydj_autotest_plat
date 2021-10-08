from django.db import models
from product.models import Product 
# Create your models here.

class Apis(models.Model):
    # 关联产品id，其中product是应用名，Product是product应用的表名
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    #  接口标题    
    apiname = models.CharField('接口名称', max_length=100)
    #  接口地址    
    apiurl = models.CharField('URL地址', max_length=200)
    #  参数及参数的值    
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    # 请求方式
    REQUEST_METHOD = (('0', 'get'),('1', 'post'),('2', 'put'),('3', 'delete'),('4', 'patch'),)
    #  请求方法
    apimethod = models.CharField(verbose_name='请求方法', choices = REQUEST_METHOD, default = 'get', max_length=200, null=True)
    #  预期结果
    apiresult = models.CharField('预期结果', max_length=200)
    #  测试结果
    apistatus = models.BooleanField('是否通过')
    #  创建时间 自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now=True)
    class Meta:
        verbose_name = u'单一场景接口'
        verbose_name_plural = u'单一场景接口'
    def __str__(self):
        return self.apiname
# class Apitest(models.Model):

#     Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)

#     # 关联产品id，其中product是应用名，Product是product应用的表名
#     # 流程接口测试场景
#     apitestname = models.CharField('流程接口名称', max_length=64)
#     # 流程接口描述
#     apitestdesc = models.CharField('描述', max_length=64, null=True)
#     # 执行人
#     apitester = models.CharField('测试负责人', max_length=16)
#     # 流程接口测试结果
#     apitestresult = models.BooleanField('测试结果')
#     # 创建时间 自动获取当前时间
#     create_time = models.DateTimeField('创建时间', auto_now=True)


#     class  Meta:

#         verbose_name = u'流程场景接口'
#         verbose_name_plural = '流程场景接口'

#         def __str__(self):
#             return self.apitestname


# class Apistep(models.Model):
#     # 关联接口
#     Apitest = models.ForeignKey('Apitest', on_delete=models.CASCADE)
#     #  接口标题    
#     apiname = models.CharField('接口名称', max_length=100)
#     #  接口地址    
#     apiurl = models.CharField('URL地址', max_length=200)
#     #  测试步骤    
#     apistep = models.CharField('测试步骤', max_length=100, null=True)
#     #  参数及参数的值    
#     apiparamvalue = models.CharField('请求参数和值', max_length=800)

#     REQUEST_METHOD = (('get', 'get'),('post', 'post'),('put', 'put'),('delete', 'delete'),('patch', 'patch'),)
#     #  请求方法
#     apimethod = models.CharField(verbose_name='请求方法', choices = REQUEST_METHOD, default = 'get', max_length=200, null=True)
#     #  预期结果
#     apiresult = models.CharField('预期结果', max_length=200)
#     #  测试步骤
#     apistep = models.CharField('测试步骤', max_length=100, null=True)
#     #  测试结果
#     apistatus = models.BooleanField('是否通过')
#     #  创建时间 自动获取当前时间
#     create_time = models.DateTimeField('创建时间', auto_now=True)

#     def __str__(self):
#         return self.name


class Apitest(models.Model):

    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)

    # 关联产品id，其中product是应用名，Product是product应用的表名
    # 流程接口测试场景
    apitestname = models.CharField('流程接口名称', max_length=64)
    # 流程接口描述
    apitestdesc = models.CharField('描述', max_length=64, null=True)
    # 执行人
    # apitester = models.CharField('测试负责人', max_length=16)
    apitester = models.CharField('执行人', max_length=16)
    # 流程接口测试结果
    apitestresult = models.BooleanField('测试结果')
    # 创建时间 自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.apitestname

    class  Meta:

        verbose_name = u'流程场景接口'
        verbose_name_plural = u'流程场景接口'




class Apistep(models.Model):

    #  关联接口ID
    Apitest = models.ForeignKey('Apitest', on_delete=models.CASCADE)
    #  接口标题    
    apiname = models.CharField('接口名称', max_length=100)
    #  测试步骤    
    apistep = models.CharField('测试步骤', max_length=100, null=True)
    #  接口地址    
    apiurl = models.CharField('URL地址', max_length=200)
    #  参数及参数的值    
    apiparamvalue = models.CharField('请求参数和值', max_length=800)

    #    REQUEST_METHOD = (('get', 'get'),('post', 'post'),('put', 'put'),('delete', 'delete'),('patch', 'patch'),)
    #  请求方法
    #    apimethod = models.CharField(verbose_name='请求方法', choices = REQUEST_METHOD, default = 'get', max_length=200, null=True)
    apimethod = models.CharField(verbose_name='请求方法', max_length=200)
    #  预期结果
    apiresult = models.CharField('预期结果', max_length=200)
    #  测试结果
    apistatus = models.BooleanField('是否通过')
    #  创建时间 自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.apiname