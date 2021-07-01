# from django.conf.urls import url

import ordersapp.views as ordersapp
from django.urls import path

app_name = "ordersapp"

urlpatterns = [
    path('',ordersapp.OrderList.as_view(), name='orders_list'),
    path('update/<pk>/',ordersapp.OrderUpdate.as_view(), name='order_update'),
    path('create/',ordersapp.OrderCreate.as_view(), name='orders_detail'),
    path('dalete/<pk>/',ordersapp.OrderDelete.as_view(), name='order_delete'),
    path('read/<pk>/',ordersapp.OrderRead.as_view(), name='order_read'),
    path('forming/complete/<pk>',ordersapp.forming_complete, name='forming_complete'),


]
