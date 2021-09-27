# Generated by Django 3.2.7 on 2021-09-24 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, verbose_name='创建时间')),
                ('productname', models.CharField(max_length=64, verbose_name='产品名称')),
                ('productdesc', models.CharField(max_length=200, verbose_name='产品描述')),
                ('productder', models.CharField(max_length=200, verbose_name='产品负责人')),
            ],
        ),
    ]