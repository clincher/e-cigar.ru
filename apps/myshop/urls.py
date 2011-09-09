
#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from shop.views.checkout import ThankYouView, ShippingBackendRedirectView,\
    PaymentBackendRedirectView
from shop.views.order import OrderListView, OrderDetailView
from shop.views.product import ProductDetailView

from apps.myshop.models import Manufacturer
from apps.myshop.models import Cartridge, Accessory
from apps.myshop.views import CigaretteListView, MyCheckoutSelectionView,\
    ProductVoteView


urlpatterns = patterns('',
    # Products
    url(r'rating/vote/$',
        ProductVoteView.as_view(),
        name='product_vote'
        ),
    url(r'^kat.html$',
        ListView.as_view(model=Manufacturer),
        name='manufacturer_list'
        ),
    url(r'^cartridges.html$',
        ListView.as_view(model=Cartridge),
        name='cartridge_list'
        ),
    url(r'^accessories.html$',
        ListView.as_view(model=Accessory),
        name='accessory_list',
        ),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+).html$',
        CigaretteListView.as_view(),
        name='manufacturer_product_list'
        ),
    url(r'^kat_(?P<slug>[0-9A-Za-z-_.//]+).php$',
        ProductDetailView.as_view(),
        name='product_detail'
        ),
    (r'^pay/', include('shop.payment.urls')),
    (r'^ship/', include('shop.shipping.urls')),

    # Checkout
    url(r'^checkout/$', MyCheckoutSelectionView.as_view(),
        name='checkout_selection' # First step of the checkout process
        ),
    url(r'^checkout/ship/$', ShippingBackendRedirectView.as_view(),
        name='checkout_shipping' # First step of the checkout process
        ),
    url(r'^checkout/pay/$', PaymentBackendRedirectView.as_view(),
        name='checkout_payment' # First step of the checkout process
        ),
    url(r'^checkout/thank_you/$', ThankYouView.as_view(),
        name='thank_you_for_your_order' # Second step of the checkout process
        ),
    # Orders
    url(r'^orders/$',
        OrderListView.as_view(),
        name='order_list'),
    url(r'^orders/(?P<pk>\d+)/$',
        OrderDetailView.as_view(),
        name='order_detail'),
    (r'^shop/cart/', include('apps.myshop.cart_urls')),
)
