from django.db import models
from django.urls import reverse


class Client(models.Model):
    """ This Model stores the names of the Clients """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ This Model stores the Product made ex. visitng card, menu car etc """
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    """ This Model contains all the orders placed by various Clients """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    date_of_order = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.client.name + '-' + self.product.product_name + '-' + str(self.date_of_order.date())
    
    def get_absolute_url(self):
        return reverse('payments:order-detail', kwargs={'pk': self.pk})

