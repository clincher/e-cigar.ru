from django.conf import settings
#from django.contrib.contenttypes.models import ContentType
from django.db.models.aggregates import Count, Min
#from shop.models import ORDERITEM_MODEL, PRODUCT_MODEL
#from shop.util.loader import load_class
from livesettings import config_value

from apps.myshop.shipping.backends.delivery_in_moscow import \
    DeliveryInMoscowShipping
from models import Cigarette, Manufacturer

def manufacturers(request):
    return {'manufacturers':
        Manufacturer.objects.annotate(min_price=Min('cigarette__unit_price'))}

def cigarettes(request):
    return {'cigarettes': Cigarette.objects.select_related(
        'manufacturer__name')}

#def most_popular_product(request):
#    OrderItem = load_class(ORDERITEM_MODEL)
#    Product = load_class(PRODUCT_MODEL)
#    cigarette_contenttype = ContentType.objects.get_for_model(Cigarette)
#    if OrderItem.objects.exists():
#        most_popular_product_id = (OrderItem.objects.
#            filter(product__polymorphic_ctype=cigarette_contenttype).
#            values('product').annotate(count=Count('id')).
#            order_by('-count')[0]['product'])
#        most_popular_product = Product.objects.select_related(
#            'manufacturer').get(pk=most_popular_product_id)
#    else :
#        most_popular_product = None
#
#    return {'most_popular_product': most_popular_product}
#
#def most_discount_product(request):
#    try:
#        most_discount = Cigarette.objects.filter(
#            discount__gt='0').select_related(
#            'manufacturer__name').order_by('-discount')[0]
#    except IndexError:
#        most_discount = None
#    return {'most_discount_product': most_discount}

def special_cigarettes(request):
    def get(key):
        try:
            return Cigarette.objects.get(slug=config_value('shop', key))
        except Cigarette.DoesNotExist:
            return None
    return {
        'most_popular_cigarette': get('MOST_POPULAR_CIGARETTE'),
        'most_discount_cigarette': get('MOST_DISCOUNT_CIGARETTE'),
        'best_male_cigarette': get('BEST_MALE_CIGARETTE'),
        'best_female_cigarette': get('BEST_FEMALE_CIGARETTE')
    }

def rating_range(request):
    return {'rating_range': range(settings.RATING_RANGE)}

def delivery_in_moscow_backend(request):
    return {
        'free_delivery_amount': DeliveryInMoscowShipping.FREE_DELIVERY_AMOUNT
    }
