# encoding : utf-8
'''
@author: jly
@file : urls.py
@time: 2018/11/14 17:28
'''

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^market/(\d+)/(\d+)/(\d+)$', market, name='market'),
    url(r'^mine/$', mine, name='mine'),
    url(r'^register/$', register, name='register'),
    url(r'^registerHandle/$', registerHandle, name='registerHandle'),  # 注册操作
    url(r'^login/$', login, name='login'),
    url(r'^loginHandle/$', loginHandle, name='loginHandle'),
    url(r'^logout/$', logout, name='logout'),  # 登出
    url(r'^checkUserName/$', checkUserName, name='checkUserName'),
    url(r'^addGoodsToCart/$', addGoodsToCart, name='addGoodsToCart'),
    url(r'^cartNumAdd/$', cartNumAdd, name='cartNumAdd'),
    url(r'^cartNumReduce/$', cartNumReduce, name='cartNumReduce'),
    url(r'^cartDelete/$', cartDelete, name='cartDelete'),
    url(r'^cartSelectOrNot/$', cartSelectOrNot, name='cartSelectOrNot'),
    url(r'^cartSelectAllOrNone/$', cartSelectAllOrNone, name='cartSelectAllOrNone'),
    url(r'^order/(\d+)/$', order, name='order'),
    url(r'^orderAdd/$', orderAdd, name='orderAdd'),
    url(r'^changeOrderStatus/$', changeOrderStatus, name='changeOrderStatus'),
    url(r'^orderUnreceive/$', orderUnreceive, name='orderUnreceive'),
]