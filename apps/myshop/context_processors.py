from django.conf import settings
from django.db.models.aggregates import Count, Min
from shop.models import ORDERITEM_MODEL, PRODUCT_MODEL
from shop.util.loader import load_class

from models import Cigarette, Manufacturer


def manufacturers(request):
    return {'manufacturers':
        Manufacturer.objects.annotate(min_price=Min('cigarette__unit_price'))}

def most_popular_product(request):
    OrderItem = load_class(ORDERITEM_MODEL)
    Product = load_class(PRODUCT_MODEL)
    if OrderItem.objects.exists():
        most_popular_product_id = OrderItem.objects.values('product').annotate(
            count=Count('id')).order_by('-count')[0]['product']
        most_popular_product = Product.objects.get(pk=most_popular_product_id)
    else :
        most_popular_product = None
        
    return {'most_popular_product': most_popular_product}

def most_discount_product(request):
    if Cigarette.objects.filter(discount__gt='0').exists():
        most_discount = Cigarette.objects.filter(
            discount__gt='0').order_by('-discount')[0]
    else:
        most_discount = None

    return {'most_discount_product': most_discount}

def rating_range(request):
    return {'rating_range': range(settings.RATING_RANGE)}