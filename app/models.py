from django.db import models

# Create your models here.

# 基类
class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True


# 轮播图
class MainWheel(Main):
    class Meta:
        db_table = 'axf_wheel'


# 导航
class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'


# 必买
class MainMustBuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


# 商店
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'

class MainShow(Main):
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=300)
    childcid1 = models.CharField(max_length=50)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)

    img2 = models.CharField(max_length=300)
    childcid2 = models.CharField(max_length=50)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)

    img3 = models.CharField(max_length=300)
    childcid3 = models.CharField(max_length=50)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'

class FoodType(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=50)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=30)
    productlongname = models.CharField(max_length=50)
    isxf = models.BooleanField()

    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=20)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=20)
    dealerid = models.CharField(max_length=20)

    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    icon = models.ImageField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    num = models.IntegerField(default=1)
    selected = models.BooleanField(default=1)

#订单
class Order(models.Model):
    orderid = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)

    #0未支付 1已支付 2代收货 3未评价
    status = models.CharField(max_length=10,default=0)

#商品订单表
class OrderGoods(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    num = models.IntegerField(default=1)
    price = models.FloatField(default=0)