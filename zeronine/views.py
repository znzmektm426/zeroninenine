from datetime import date, datetime
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

from zeronine.forms import *
from zeronine.models import *

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    join = Join.objects.all()
    join_detail = JoinDetail.objects.all()
    products = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    designated_low = Designated.objects.filter(rep_price='True').order_by('price')
    designated_high = Designated.objects.filter(rep_price='True').order_by('-price')
    product_due_date = Product.objects.all().order_by('due_date')
    product_created_at = Product.objects.all().order_by('-created_at')

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category_code=current_category)


    return render(request, 'zeronine/list.html', {'current_category': current_category,
                                                  'categories':categories,
                                                  'products':products,
                                                  'join':join,
                                                  'join_detail':join_detail,
                                                  'designated_object':designated_object,
                                                  'designated_high': designated_high,
                                                  'designated_low': designated_low,
                                                  'product_due_date':product_due_date,
                                                  'product_created_at':product_created_at,
                                                  })

def product_detail(request, id, product_slug=None):
    current_category = None
    categories = Category.objects.all()
    product = get_object_or_404(Product, product_code=id, slug=product_slug)
    product_object = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    designated_object2 = Designated.objects.filter(rep_price='False', product_code=id)
    element_object = Element.objects.all()
    photo_object = Photo.objects.all()
    option_object = Option.objects.all()
    value_object = Value.objects.all()
    delta = product.due_date - datetime.now().date()
    delta_result = delta.days


    return render(request, 'zeronine/detail.html', {'product': product,
                                                    'product_object':product_object,
                                                    'current_category': current_category,
                                                    'categories': categories,
                                                    'designated_object': designated_object,
                                                    'designated_object2':designated_object2,
                                                    'element_object': element_object,
                                                    'photo_object':photo_object,
                                                    'option_object': option_object,
                                                    'value_object': value_object,
                                                    'delta': delta,
                                                    'delta_result': delta_result,
                                                    })

