# -*- coding: utf-8 -*-
#from shop.models import Cart
from shop.models.defaults.bases import BaseCart


class MyCart(BaseCart):
    class Meta(object):
        pass

    def update_quantity(self, cart_item_id, quantity):
        """
        Updates the quantity for given cart item
        """
        cart_item = self.items.get(pk=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()
        self.save()