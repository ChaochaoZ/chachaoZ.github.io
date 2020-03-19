from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

#数据库是重中之重
#一对多的关系，是用外键进行关联的
class Medicine(models.Model):
	name = models.CharField(max_length=200)
	sn = models.CharField(max_length=200)
	desc = models.CharField(max_length=200)

#一个顾客多条订单
import datetime
# class Order(models.Model):
# 	name = models.CharFiled(max_length=200,null=True,blank=True)
# 	create_date = models.DateTimeField(default=datetime.datetime.now)
# 	customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
#一对一
#用的是models.OneToOneField(Student,on_delete=models.PROTECT)
#多对多
import datetime
class Order(models.Model):
	name = models.CharField(max_length=200,null=True,blank=True)
	create_date = models.DateTimeField(default=datetime.datetime.now)
	customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
	#并不会出现一个medicine的字段，而是通过另一个表来确定的
	medicines = models.ManyToManyField(Medicine,through='OrderMedicine')
class OrderMedicine(models.Model):
	#两个外键
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    amount = models.PositiveIntegerField()




















