from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Client, Product, Order
from .forms import ClientModelForm, ProductModelForm, OrderModelForm


class ClientListView(ListView):
    template_name = 'payments/client_list.html'
    queryset = Client.objects.all()


class ProductListView(ListView):
    template_name = 'payments/product_list.html'
    queryset = Product.objects.all()


class OrderListView(ListView):
    template_name = 'payments/order_list.html'
    queryset = Order.objects.all()


class OrderDetailView(DetailView):
    template_name = 'payments/order_detail.html'
    queryset = Order.objects.all()


class OrderCreateView(CreateView):
    template_name = 'payments/order_create.html'
    form_class = OrderModelForm
    queryset = Order.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
