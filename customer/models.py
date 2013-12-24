from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class Custmer(models.Model):
    name = models.CharField(max_length=100)

    billing_address = models.ForeignKey(
        Address,
        related_name='billing_customer_set')
    shipping_address = models.ForeignKey(
        Address,
        related_name='shipping_customer_set')
