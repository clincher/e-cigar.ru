# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.utils.translation import ugettext as _
from shop.util.address import assign_address_to_request
from shop.views.checkout import CheckoutSelectionView
from shop.models import Product, CartItem
from shop.util.cart import get_or_create_cart
from shop_simplevariations.models import CartItemTextOption, CartItemOption
from shop_simplevariations.views import SimplevariationCartDetails

from apps.common.views import JSONResponseMixin
from apps.myshop.models import Cigarette, Manufacturer, Cartridge
from apps.myshop.signals import payment_instructions_email_notification


class CigaretteListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(
            CigaretteListView, self).get_context_data(**kwargs)
        if 'slug' in self.kwargs:
            try:
                context['manufacturer'] = Manufacturer.objects.get(
                    slug=self.kwargs['slug'])
            except Manufacturer.DoesNotExist:
                pass
        return context

    def get_queryset(self):
        filter = dict(active=True)
        if 'slug' in self.kwargs:
            filter.update(manufacturer__slug=self.kwargs['slug'])
        return Cigarette.objects.filter(**filter)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(
                _(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list)
        if 'slug' in self.kwargs and 'manufacturer' not in context:
            raise Http404(u'Страница не найдена')
        return self.render_to_response(context)


class MyCheckoutSelectionView(CheckoutSelectionView):

    def post(self, *args, **kwargs):
        """ Called when view is POSTed """
        shipping_form = self.get_shipping_address_form()
        if shipping_form.is_valid():

            # Add the address to the order
            shipping_address = shipping_form.save()
            order = self.create_order_object_from_cart()

            self.save_addresses_to_order(order, shipping_address,
                                         shipping_address)

            assign_address_to_request(self.request, shipping_address)
            assign_address_to_request(self.request, shipping_address,
                                      shipping=False)

            billingshipping_form = (
                self.get_billing_and_shipping_selection_form())
            if billingshipping_form.is_valid():
                self.request.session['payment_backend'] = (
                    billingshipping_form.cleaned_data['payment_method'])
                self.request.session['shipping_backend'] = (
                    billingshipping_form.cleaned_data['shipping_method'])
                payment_instructions_email_notification(
                    order=order,
                    address=shipping_address,
                    request=self.request
                )
                return HttpResponseRedirect(reverse('checkout_shipping'))

        return self.get(self, *args, **kwargs)


class MySimplevariationCartDetails(SimplevariationCartDetails):
    def post(self, *args, **kwargs):
        #it starts similar to the original post method
        product_id = self.request.POST['add_item_id']
        product_quantity = self.request.POST.get('add_item_quantity')
        if not product_quantity:
            product_quantity = 1
        product = Product.objects.get(pk=product_id)
        cart_object = get_or_create_cart(self.request)

        #now we need to find out which options have been chosen by the user
        option_ids = []
        text_option_ids = {} # A dict of {TextOption.id:CartItemTextOption.text}
        for key in self.request.POST.keys():
            if key.startswith('add_item_option_group_'):
                option_ids.append(self.request.POST[key])
            elif key.startswith('add_item_text_option_'):
                id = key.split('add_item_text_option_')[1]
                text_option_ids.update({id:self.request.POST[key]})

        #now we need to find out if there are any cart items that have the exact
        #same set of options
        qs = CartItem.objects.filter(cart=cart_object).filter(product=product)
        found_cartitem_id = None
        merge = False
        for cartitem in qs:
            # for each CartItem in the Cart, get it's options and text options
            cartitemoptions = CartItemOption.objects.filter(
                cartitem=cartitem, option__in=option_ids
                )

            cartitemtxtoptions = CartItemTextOption.objects.filter(
                text_option__in=text_option_ids.keys(),
                text__in=text_option_ids.values()
                )

            if (len(cartitemoptions) + len(cartitemtxtoptions)
                == (len(option_ids) + len(text_option_ids))):
                found_cartitem_id = cartitem.id
                merge = True
                break

        #if we found a CartItem object that has the same options, we need
        #to select this one instead of just any CartItem that belongs to this
        #cart and this product.
        if found_cartitem_id:
            qs = CartItem.objects.filter(pk=found_cartitem_id)

        cart_item = cart_object.add_product(
            product, product_quantity, merge=merge, queryset=qs)
        if isinstance(product, Cigarette):
            try:
                cart_object.add_product(product.cartridge, 0)
                for accessory in product.accessories.all():
                    cart_object.add_product(accessory, 0)
            except Cartridge.DoesNotExist, AttributeError:
                pass

        cart_object.save()
        return self.post_success(product, cart_item)


class ProductVoteView(JSONResponseMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            product = Cigarette.objects.get(pk=int(request.GET['product']))
            product.rating.add(int(request.GET['score']), request.user,
                           request.META['REMOTE_ADDR'], request.COOKIES)
        except :
            pass #nothing terrible
        return super(ProductVoteView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return {'result': 'ok'}