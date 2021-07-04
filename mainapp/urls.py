# from django.conf.urls import url

import mainapp.views as mainapp
from django.urls import re_path, path

app_name="mainapp"

urlpatterns = [
    # re_path(r'^$', mainapp.products, name='index'),
    # re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
    # re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    #
    # re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
    path('', mainapp.products, name='index'),
    path('category/<pk>/', mainapp.products, name='category'),
    path('product/<pk>/', mainapp.product, name='product'),
    path('category/<pk>/page/<page>/', mainapp.products, name='page'),

]

    