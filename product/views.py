from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from zeronine.models import *
from .forms import *

# Create your views here.
def product_upload(request):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    photos = Photo.objects.all()
    designated_object = Designated.objects.all()
    options = Option.objects.all()
    slug = Product.slug

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = Product()
            product.name = form.cleaned_data['name']
            product.benefit = form.cleaned_data['benefit']
            product.detail = form.cleaned_data['detail']
            product.target_price = form.cleaned_data['target_price']
            product.start_date = form.cleaned_data['start_date']
            product.due_date = form.cleaned_data['due_date']
            product.category_code = form.cleaned_data['category_code']
            product.image = request.FILES['photo']
            product.username = request.user
            product.slug = slug
            product.kakao_link = form.cleaned_data['kakao_link']
            product.save()

        for img in request.FILES.getlist('image'):
            photo = Photo()
            photo.product_code = product
            photo.photo = img
            photo.save()

    if request.method == "POST":
        form = OptionForm(request.POST)

        if form.is_valid():
            option = Option()
            option.name = form.cleaned_data['option_name']
            option.product_code = product
            option.save()

    if request.method == "POST":
        form = ValueForm(request.POST)

        if form.is_valid():
            value = Value()
            value.name = form.cleaned_data['value_name']
            value.option_code = option
            value.product_code = product
            value.extra_cost = form.cleaned_data['option_price']
            value.save()

    if request.method == "POST":
        form = ValueForm(request.POST)

        if form.is_valid():
            value = Value()
            value.name = form.cleaned_data['second_value']
            value.option_code = option
            value.product_code = product
            value.extra_cost = form.cleaned_data['second_option_price']
            value.save()

    if request.method == "POST":
        form = ValueForm(request.POST)

        if form.is_valid():
            value = Value()
            value.name = form.cleaned_data['third_value']
            value.option_code = option
            value.product_code = product
            value.extra_cost = form.cleaned_data['third_option_price']
            value.save()

    if request.method == "POST":
        form = DesignatedForm(request.POST)

        if form.is_valid():
            designated = Designated()
            designated.price = form.cleaned_data['price']
            designated.product_code = product
            designated.rep_price = True
            designated.save()


            return render(request, 'zeronine/list.html', {'form': form,
                                                          'current_category': current_category,
                                                          'photos':photos,
                                                          'options':options,
                                                          'products': products,
                                                          'categories': categories,
                                                          'slug': slug, })
    else:
        form = ProductForm()

    return render(request, 'product/product_upload.html',{'form': form,
                                                          'current_category': current_category,
                                                          'photos':photos,
                                                          'options':options,
                                                          'products': products,
                                                          'categories': categories})

def product_search(request):
    current_category = None
    categories = Category.objects.all()
    designated_object = Designated.objects.all()
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query))

    return render(request, 'product/product_search.html', {'designated_object':designated_object, 'current_category':current_category, 'categories':categories, 'query':query, 'products':products})