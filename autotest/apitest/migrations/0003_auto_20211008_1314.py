# Generated by Django 3.2.7 on 2021-10-08 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_options'),
        ('apitest', '0002_auto_20210929_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='apitest',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='apitest',
            name='apitestdesc',
            field=models.CharField(max_length=64, null=True, verbose_name='描述'),
        ),
        migrations.CreateModel(
            name='Apis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiname', models.CharField(max_length=100, verbose_name='接口名称')),
                ('apiurl', models.CharField(max_length=200, verbose_name='URL地址')),
                ('apiparamvalue', models.CharField(max_length=800, verbose_name='请求参数和值')),
                ('apimethod', models.CharField(choices=[('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch')], default='get', max_length=200, null=True, verbose_name='请求方法')),
                ('apiresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('apistatus', models.BooleanField(verbose_name='是否通过')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '单一场景接口',
                'verbose_name_plural': '单一场景接口',
            },
        ),
    ]
