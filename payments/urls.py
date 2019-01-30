from django.conf.urls import url
from django.urls import path
from .views import (
    ClientListView,
    ProductListView,
    OrderListView,
    OrderDetailView,
    OrderCreateView,
)


app_name = 'payments'


urlpatterns = [
    path('clients/', ClientListView.as_view(), name='clients'),
    path('products/', ProductListView.as_view(), name='products'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('neworder/', OrderCreateView.as_view(), name='new-order'),
]
