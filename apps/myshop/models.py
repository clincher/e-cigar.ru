# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from shop.order_signals import completed
from djangoratings.fields import AnonymousRatingField
from apps.myshop.base.models import BaseProductParameter, BaseProduct, BaseProductImage

from signals import confirmed_email_notification


class Manufacturer(BaseProductParameter):
    """Master data: Information about manufacturers."""
    service_center = models.BooleanField(
        verbose_name=u'Наличие сервисного центра в Москве')

    class Meta:
        app_label = 'myshop'
        verbose_name = u'Производитель'
        verbose_name_plural = u'Производители'


class Flavour(BaseProductParameter):
    """Master data: Information about cigarettes and cartridge flavours"""

    class Meta:
        app_label = 'myshop'
        verbose_name = u'Вкус'
        verbose_name_plural = u'Вкусы'


class Cartridge(BaseProduct):
    """Master data: info about cartridges"""
    flavours = models.ManyToManyField(Flavour,
        verbose_name=u'Выберите варианты вкусов для этого картриджа')

    class Meta:
        app_label = 'myshop'
        verbose_name = u'Картридж'
        verbose_name_plural = u'Картриджи'


class CartridgeImage(BaseProductImage):
    cartridge = models.ForeignKey(Cartridge, related_name='images')

    class Meta:
        app_label = 'myshop'


class Cigarette(BaseProduct):
    """Master data: info about cigarette"""
    discount = models.DecimalField(verbose_name=u'Скидка', max_digits=6,
                                   decimal_places=2, default=0.0)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name=u'Производитель')
    default_flavour = models.ForeignKey(Flavour, verbose_name=u'Вкус по умолчанию')
    cartridge = models.OneToOneField(Cartridge, verbose_name=u'Картридж',
                                     related_name='cigarette')
    length = models.PositiveIntegerField(verbose_name=u'Длина в сантиметрах',
                                         null=True, blank=True)
    diameter = models.PositiveIntegerField(verbose_name=u'Диаметр в миллиметрах',
                                           null=True, blank=True)
    weight = models.PositiveIntegerField(verbose_name=u'Вес в граммах',
                                         null=True, blank=True)
    conditional_number = models.PositiveIntegerField(
        verbose_name=u'Условное количество обычных сигарет', null=True, blank=True)
    battery_capacity = models.PositiveIntegerField(
        verbose_name=u'Ёмкость аккумулятора', null=True, blank=True)
    full_recharge = models.CharField(max_length=10,
        verbose_name=u'Время полной зарядки аккумулятора', null=True, blank=True)
    color = models.CharField(max_length=20,
                             verbose_name=u'Цвет сигареты', null=True, blank=True)
    rating = AnonymousRatingField(range=settings.RATING_RANGE, use_cookies=True)

    class Meta:
        app_label = 'myshop'
        verbose_name = u'Сигарета'
        verbose_name_plural = u'Сигареты'

    def __unicode__(self):
        return self.get_full_name()

    def service_center(self):
        return self.manufacturer.service_center

    def flavours(self):
        return self.cartridge.flavours

    def get_full_name(self):
        return u'{0} {1}'.format(self.manufacturer.name, self.name)

    def old_price(self):
        return self.unit_price + self.discount


class CigaretteImage(BaseProductImage):
    cigarette = models.ForeignKey(Cigarette, related_name='images')

    class Meta:
        app_label = 'myshop'


class Accessory(BaseProduct):
    """Master data: info about accessories"""
    related_cigarettes = models.ManyToManyField(Cigarette,
        related_name='accessories', blank=True, null=True,
        verbose_name=u'Сигареты, к которым подходит этот аксессуар')

    class Meta:
        app_label = 'myshop'
        verbose_name = u'Аксессуар'
        verbose_name_plural = u'Аксессуары'


class AccessoryImage(BaseProductImage):
    accessory = models.ForeignKey(Accessory, related_name='images')

    class Meta:
        app_label = 'myshop'


completed.connect(confirmed_email_notification)