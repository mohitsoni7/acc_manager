from django import forms
from .models import Client, Product, Order


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderModelForm(forms.ModelForm):
    client = forms.CharField(max_length=100)
    product = forms.CharField(max_length=100)
    class Meta:
        model = Order
        fields = ['client', 'product', 'description', 'quantity', 'rate']
    