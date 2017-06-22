from __future__ import unicode_literals

from django.db import models

# Create your models here.

# import default models from shop to materialize them
from shop.models.defaults.address import ShippingAddress, BillingAddress
from shop.models.defaults.cart import Cart
from shop.models.defaults.cart_item import CartItem
from shop.models.defaults.customer import Customer

from shop.models.defaults.order_item import OrderItem
