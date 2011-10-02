#-*- coding: utf-8 -*-
from decimal import Decimal

from django.conf import settings
from shop.cart.cart_modifiers_base import BaseCartModifier

from apps.myshop.models import Cigarette


class CigaretteQuantityRebateModifier(BaseCartModifier):

    def get_extra_cart_item_price_field(self, cart_item):
        """
        Add a rebate to a cigarette depending on quantity ordered cigarettes
        """

        if not isinstance(cart_item.product, Cigarette):
            return None

        cigarette_ordered_count = sum([item.quantity
            for item in cart_item.cart.items.all()
            if isinstance(item.product, Cigarette)
        ])
        
        if not cigarette_ordered_count:
            return None

        template = u'Скидка за покупку {0} сигарет {1}%'
        rebate_percentage = self.get_rebate_percentage(cigarette_ordered_count)
        rebate = self.get_rebate_by_cigarette_count(
            cart_item, rebate_percentage)

        return template.format(
            cigarette_ordered_count, rebate_percentage), -rebate

    def get_rebate_percentage(self, count):
        REBATES = settings.REBATE_PERCENTAGES
        try:
            return REBATES[count]
        except KeyError:
            return REBATES[max(REBATES.keys())]

    def get_rebate_by_cigarette_count(self, cart_item, rebate_percentage):
        # rebate calculate
        return (Decimal(rebate_percentage)/100) * cart_item.line_subtotal
