from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from join.forms import *
from zeronine.models import *

# Create your views here.

def join_create(request, id):
    current_category = None
    designated = Designated.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    value_p = Value.extra_cost
    element = Element.objects.all()
    value_object = Value.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == "POST":
            product = Product.objects.get(product_code=id)
            join = Join()
            join.product_code = product
            join.username = request.user
            join.save()

            if request.method == "POST":
                form = ElementForm(request.POST)

                if form.is_valid():
                    for value_code2 in request.POST.getlist('value_code2'):
                        element = Element()
                        element.designated_code = Designated.objects.get(product_code=id)
                        element.value_code = get_object_or_404(Value, pk=value_code2)
                        element.save()

                else:
                    element = Element()
                    element.designated_code = Designated.objects.get(product_code=id)
                    element.value_code = None
                    element.save()

            if request.method == "POST":
                form = JoinDetailForm(request.POST)

                if form.is_valid():
                    for quantity, price2, value_code2 in zip(request.POST.getlist('quantity'), request.POST.getlist('price2'), request.POST.getlist('value_code2')):
                        join_detail = JoinDetail()
                        join_detail.join_code = join
                        join_detail.designated_code = Designated.objects.get(product_code=id)
                        join_detail.value_code = get_object_or_404(Value, pk=value_code2)
                        join_detail.quantity = quantity
                        join_detail.price = price2
                        join_detail.save()

                else:
                    join_detail = JoinDetail()
                    join_detail.join_code = join
                    join_detail.designated_code = Designated.objects.get(product_code=id)
                    join_detail.quantity = request.POST.get('quantity')
                    join_detail.price = request.POST.get('price2')
                    join_detail.value_code = None
                    join_detail.save()

                return render(request, 'zeronine/list.html', {'current_category': current_category,
                                                              'products': products,
                                                              'categories': categories,
                                                              'designated': designated})


    return render(request, 'zeronine/detail.html', {'products':products,
                                                    'designated': designated,
                                                    'element': element,
                                                    'value_p':value_p,
                                                    'designated_object':designated_object,
                                                    'value_object': value_object})