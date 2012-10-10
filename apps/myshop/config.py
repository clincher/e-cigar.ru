# -*- coding: utf-8 -*-

from livesettings import (config_register, ConfigurationGroup,
                          PositiveIntegerValue)
from django.utils.translation import ugettext_lazy as _

# First, setup a grup to hold all our possible configs
SHOP_GROUP = ConfigurationGroup('shop', _('Shop Settings'), ordering=0)

# Now, add our number of images to display value
# If a user doesn't enter a value, default to 5
config_register(PositiveIntegerValue(
    SHOP_GROUP,
    'MOST_DISCOUNT_CIGARETTE',
    description = u'Самое выгодное предложение',
    help_text = u'Укажите численный идентификатор продукта (можно посмотреть в'
                u' строке адреса',
    default = 56
))
config_register(PositiveIntegerValue(
    SHOP_GROUP,
    'MOST_POPULAR_CIGARETTE',
    description = u'Самая популярная сигарета',
    help_text = u'Укажите численный идентификатор продукта (можно посмотреть в'
                u' строке адреса',
    default = 26
))
config_register(PositiveIntegerValue(
    SHOP_GROUP,
    'BEST_MALE_CIGARETTE',
    description = u'Лучшая мужская сигарета',
    help_text = u'Укажите численный идентификатор продукта (можно посмотреть в'
                u' строке адреса',
    default = 5
))
config_register(PositiveIntegerValue(
    SHOP_GROUP,
    'BEST_FEMALE_CIGARETTE',
    description = u'Лучшая женская сигарета',
    help_text = u'Укажите численный идентификатор продукта (можно посмотреть в'
                u' строке адреса',
    default = 5
))
