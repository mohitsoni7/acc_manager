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
    class Meta:
        model = Order
        fields = ['client', 'product', 'description', 'quantity', 'rate']


class OrderForm(forms.Form):
    client = forms.CharField(label='Client')
    product = forms.CharField(label='Product')
    