
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from Mail.settings import MEDIA_ROOT
from .models import *
import os, hashlib, uuid

#首页
def home(request):
    #轮播图数据
    wheels = MainWheel.objects.all()

    #导航
    navs = MainNav.objects.all()

    #mustBuy
    mustBuys = MainMustBuy.objects.all()

    # shop
    shop = MainShop.objects.all()
    shop0 = shop[0]
    shop1_2 = shop[1:3]
    shop3_6 = shop[3:7]
    shop7_10 = shop[7:11]

    #mainShow
    shows = MainShow.objects.all()
    data = {
        'wheels': wheels,
        'navs': navs,
        'mustBuys': mustBuys,
        'shop0': shop0,
        'shop1_2': shop1_2,
        'shop3_6': shop3_6,
        'shop7_10': shop7_10,
        'shows': shows,
    }
    return render(request, 'home/home.html', data)

#闪购
def market(request, typeid, childTypeid, sortid):

        # 分类数据
        foodTypes = FoodType.objects.all()

        foodType = foodTypes.get(typeid=typeid)  # 一条分类数据

        # 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540
        # [全部分类:0,酸奶乳酸菌:103537,牛奶豆浆:103538,面包蛋糕:103540]
        # [[全部分类,0],[酸奶乳酸菌,103537],[牛奶豆浆,103538],[面包蛋糕,103540]]
        childTypes = foodType.childtypenames  # 子分类
        print(childTypes)
        childTypesList = childTypes.split('#')

        childTypesList = [childType.split(':') for childType in childTypesList]
        print(childTypesList)

        # 商品
        goods = Goods.objects.filter(categoryid=typeid)

        # 当子分类不是0时再筛选子分类商品
        if childTypeid != '0':
            goods = goods.filter(childcid=childTypeid)

        # 根据排序id筛选商品

        # 综合排序
        if sortid == '0':
            pass
        # 销量排序
        elif sortid == '1':
            goods = goods.order_by('-productnum')
        # 价格降序
        elif sortid == '2':
            goods = goods.order_by('-price')
        # 价格升序
        elif sortid == '3':
            goods = goods.order_by('price')

        data = {
            'foodTypes': foodTypes,
            'goods': goods,
            'typeid': typeid,
            'childTypesList': childTypesList,
            'childTypeid': childTypeid,
        }
        return render(request, 'market/market.html', data)

#购物车
def cart(request):
    return render(request, 'cart/cart.html')

#购物车添加商品
def addGoodsToCart(request):


    data = {
        'status':1,
        'msg':'添加成功'
    }
    userid = request.session.get('userid')

    #没有登录
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    #已经登录
    else:
        if request.method == 'GET':
            goodsId = request.GET.get('goodsid')
            num = request.GET.get('num', 0)

            carts = Cart.objects.filter(user_id=userid, goods_id=goodsId)

            #如果有购物车
            if carts.exists():
                cart = carts.first()
                cart.num += int(num)
                cart.save()

            #如果没有购物车
            else:
                cart = Cart()
                cart.user_id = userid
                cart.goods_id = goodsId
                cart.num = num
                cart.save()
        else:
            data['status'] = -1
            data['msg'] = '请求方式有误'

    return JsonResponse(data)

#购物车
def cart(request):

    userid = request.session.get('userid',0)

    if not userid:
        return redirect(reverse('mail:login'))
    else:
        carts = Cart.objects.filter(user_id=userid)

        return render(request, 'cart/cart.html', {'carts': carts})

def cartNumAdd(request):
    data = {
        'status':1,
        'msg':'增加成功'
    }

    userid = request.session.get('userid')
    if not userid:
        data['status'] = 0
        data['msg'] = '没有登录'

    #已经登录
    else:
        if request.method == 'GET':

            cartid = request.GET.get('cartid')
            carts = Cart.objects.filter(id=cartid)

            if carts.exists():
                cart = carts.first()
                cart.num += 1
                cart.save()

                #把最近的数量传回到前台
                data['num'] = cart.num
            else:
                data['status'] = -1
                data['msg'] = '购物车中没有此商品'
        else:
            data['status'] = -2
            data['msg'] = '请求方式有问题'

    return JsonResponse(data)

def cartNumReduce(request):

    data = {
        'status':1,
        'msg':'成功'
    }

    userid = request.session.get('userid')

    if not userid:
        data['status'] = 0
        data['msg'] = '没有登录'
    else:

        if request.method == 'POST':
            cartid = request.POST.get('cartid')
            carts = Cart.objects.filter(id=cartid)

            if carts.exists():
                cart = carts.first()
                if cart.num > 1:
                    cart.num -= 1
                cart.save()

                data['num'] = cart.num
            else:
                data['status'] = -1
                data['msg'] = '购物车中没有此商品'
        else:
            data['status'] = -2
            data['msg'] = '请求方式不对'

    return JsonResponse(data)

#删除
def cartDelete(request):

    data = {
        'status':1,
        'msg':'删除成功'
    }

    userid = request.session.get('userid')
    if not userid:
        data['status'] = 0
        data['msg'] = '没有登录'

    #已经登录
    else:
        if request.method == 'POST':

            cartid = request.POST.get('cartid')

            Cart.objects.filter(id=cartid).delete()



        else:
            data['status'] = -2
            data['msg'] = '请求方式有问题'

    return JsonResponse(data)

#是否勾选（单个）
def cartSelectOrNot(request):
    data = {
        'status':1,
        'msg':'勾选成功'
    }

    userid = request.session.get('userid')
    if not userid:
        data['status'] = 0
        data['msg'] = '没有登录'

    #已经登录
    else:
        if request.method == 'GET':

            cartid = request.GET.get('cartid')
            carts = Cart.objects.filter(id=cartid)

            if carts.exists():
                cart = carts.first()
                cart.selected = not cart.selected
                cart.save()

                #把最近的数量传回到前台
                data['selected'] = cart.selected
            else:
                data['status'] = -1
                data['msg'] = '购物车中没有此商品'
        else:
            data['status'] = -2
            data['msg'] = '请求方式有问题'

    return JsonResponse(data)

#是否勾选（所有）
def cartSelectAllOrNone(request):

    data = {
        'status':1,
        'msg':'成功'
    }

    userid = request.session.get('userid')

    if not userid:
        data['status'] = 0,
        data['msg'] = '没有登录'
    else:
        if request.method == 'POST':

            selected = request.POST.get('selected')

            if int(selected):
                #把现在没有打钩的商品打钩
                Cart.objects.filter(user_id=userid,selected=False).update(selected=True)
            else:
                #把现在已经打钩的商品去钩
                Cart.objects.filter(user_id=userid,selected=True).update(selected=False)

        else:
            data['status'] = -1
            data['msg'] = '请求方式不对'

    return JsonResponse(data)

#订单
def order(request,oid):
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('mail:login'))
    else:
        order = Order.objects.get(id=oid)
        return render(request, 'order/order.html', {'order':order})

#生成订单
def orderAdd(request):
    data = {
        'status':1,
        'msg':'生成成功',
    }

    userid = request.session.get('userid')

    if not userid:
        data['status'] = 0,
        data['msg'] = '没有登录'
    else:
        if request.method == 'POST':
            #生成订单
            order = Order()
            order.orderid = randomGenerator()
            order.user_id = userid
            order.save()

            #筛选当前用户已经打钩的购物车
            carts = Cart.objects.filter(user_id=userid,selected=True)

            total = 0
            for cart in carts:
                orderGoods = OrderGoods()
                orderGoods.order_id = order.id
                orderGoods.goods_id = cart.goods_id
                orderGoods.num = cart.num
                orderGoods.price = cart.goods.price

                orderGoods.save()

                #计算订单总价
                total += orderGoods.num * orderGoods.price

            order.price = total

            data['orderid'] = order.id

            #清空购物车
            carts.delete()

            order.save()
        else:
            data['status'] = -2
            data['msg'] = '请求方式不对'

    return JsonResponse(data)

def orderUnreceive(request):

    userid = request.session.get('userid')

    if not userid:
        return redirect(reverse('main:login'))
    else:

        orders = Order.objects.filter(status=1)
        return render(request, 'order/order_unreceive.html', {'orders': orders})

def changeOrderStatus(request):
    data = {
        'status':1,
        'msg':'成功',
    }
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('axf:login'))
    else:
        if request.method == 'POST':
            orderid = request.POST.get('orderid')
            status = request.POST.get('status')

            Order.objects.filter(id=orderid).update(status=status)
        else:
            data['status'] = -1
            data['msg'] = '请求方式有问题'

    return JsonResponse(data)

#我的
def mine(request):
    userid = request.session.get('userid',0)
    data = {
        'username':'',
        'icon':'',
    }
    users = User.objects.filter(id=userid)
    if users:
        data['username'] = users.first().username
        data['icon'] = str(users.first().icon)
        print(data['icon'], type(data['icon']), '-'*30)
    return render(request, 'mine/mine.html', data)

def register(request):
    return render(request, 'user/register.html')

#我的MD5
def myMd5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

#随机生成函数
def randomGenerator():
    uid = str(uuid.uuid4())
    return myMd5(uid)

#注册操作
def registerHandle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        icon = request.FILES.get('iconfile')
        if password != repassword:
            return HttpResponse("输入密码不一致")
        user = User()
        user.username = username
        user.password = myMd5(password)
        user.email = email
        #随机文件名
        iconRandomName = randomGenerator() + os.path.splitext(icon.name)[1]

        iconFile = MEDIA_ROOT + iconRandomName

        if not icon:
            return HttpResponse("头像没有上传")
        with open(iconFile,'ab') as f:
            for part in icon.chunks():
                f.write(part)
                f.flush()
        user.icon = '/uploads/' + iconRandomName
        user.save()
        request.session['userid'] = user.id
        return redirect(reverse('mail:login'))

    return redirect(reverse('mail:mine'))

#检查用户名
def checkUserName(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        if User.objects.filter(username=username):
            return JsonResponse({'status': 0, 'msg': '用户名不可用'})
        else:
            return JsonResponse({'status': 1, 'msg': '用户名可用'})
    else:
        return JsonResponse({'status': -1, 'msg': '请求方式有误'})

def login(request):
    return render(request, 'user/login.html')

#登陆操作
def loginHandle(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        users = User.objects.filter(username=username, password=myMd5(password))
        if users:
            request.session['userid'] = users[0].id
            return redirect(reverse('mail:mine'))
        else:
            return HttpResponse("用户名或密码错误")
    else:
        return HttpResponse("请求方式有误")

#登出
def logout(request):
    del request.session['userid']
    return redirect(reverse('mail:mine'))
