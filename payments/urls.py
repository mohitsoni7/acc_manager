from django.conf.urls import url
from django.urls import re_path
from .views import (
    ClientListView,
    ProductListView,
    OrderListView,
    OrderDetailView,
    OrderCreateView,
)


app_name = 'payments'


urlpatterns = [
    url('clients/', ClientListView.as_view(), name='clients'),
    url('products/', ProductListView.as_view(), name='products'),
    url('orders/', OrderListView.as_view(), name='orders'),
    # url('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    re_path(r'^order/(?P<pk>[0-9]+)/$', OrderDetailView.as_view(), name='order-detail'),
    url('neworder/', OrderCreateView.as_view(), name='new-order'),
]
