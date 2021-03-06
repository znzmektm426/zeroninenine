from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from zeronine.models import *
from datetime import date, datetime


# Create your views here.

def zzim(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    zzim = Zzim.objects.all().order_by('product_code')
    join_detail_objects = JoinDetail.objects.all()
    join_objects = Join.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')

    return render(request, 'zzim/zzim_list.html', {'zzim':zzim,
                                                   'products':products,
                                                   'categories':categories,
                                                   'join_detail_objects':join_detail_objects,
                                                   'join_objects':join_objects,
                                                   'designated_object':designated_object})

def add_zzim(request, id):
    current_category = None
    designated_object = Designated.objects.all()
    element_object = Element.objects.all()
    value_object = Value.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    option_object = Option.objects.all()
    photo_object = Photo.objects.all()
    product = get_object_or_404(Product, product_code=id)
    delta = product.due_date - datetime.now().date()
    delta_result = delta.days

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == "POST":
            product = Product.objects.get(product_code=id)
            zzim = Zzim()
            zzim.product_code = product
            zzim.username = request.user
            zzim.save()

    return render(request, 'zeronine/detail.html', {'zzim':zzim,
                                                          'current_category': current_category,
                                                          'product': product,
                                                          'products': products,
                                                          'categories': categories,
                                                          'element_object': element_object,
                                                          'value_object': value_object,
                                                          'designated_object': designated_object,
                                                          'option_object':option_object,
                                                          'photo_object':photo_object,
                                                          'delta': delta,
                                                          'delta_result': delta_result,
                                                          })

    return render(request, 'zeronine/detail.html', {'zzim':zzim,
                                                    'product':product,
                                                    'designated': designated,
                                                    'element_object': element_object,
                                                    'value_object': value_object})