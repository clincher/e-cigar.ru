#-*- coding: utf-8 -*-
from decimal import Decimal

from django.conf import settings
from shop.cart.cart_modifiers_base import BaseCartModifier

from apps.myshop.models import Cigarette


class CigaretteQuantityRebateModifier(BaseCartModifier):

    def rebate_calculate(self, cart_item, rebate_percentage):
        return (Decimal(rebate_percentage)/100) * cart_item.line_subtotal

    def get_extra_cart_item_price_field(self, cart_item):
        """
        Add a rebate to a cigarette depending on the quantity cigarettes ordered:
        """
        REBATE_PERCENTAGES = settings.REBATE_PERCENTAGES
        cigarette_ordered_count = sum([item.quantity
            for item in cart_item.cart.items.all()
            if isinstance(item.product, Cigarette)
        ])

        if cigarette_ordered_count in REBATE_PERCENTAGES.keys():
            rebate_percentage = REBATE_PERCENTAGES[cigarette_ordered_count]
            rebate = self.rebate_calculate(cart_item, rebate_percentage)
            result_tuple = ('Скидка', -rebate)
        elif cigarette_ordered_count > 1:
            rebate_percentage = REBATE_PERCENTAGES[
                                max(REBATE_PERCENTAGES.keys())]
            rebate = self.rebate_calculate(cart_item, rebate_percentage)
            result_tuple = ('Скидка', -rebate)
        else :
            result_tuple = None
        return result_tuple # Returning None is ok