from datetime import datetime

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from mypage.forms import *
from zeronine.models import *

# Create your views here.

def mypage_list(request):
   current_category = None
   categories = Category.objects.all()
   member = Member.objects.all()

   if not request.user.is_authenticated:
       return HttpResponseRedirect(reverse('zeronine:login'))

   if request.method == "POST":
       for m in member:
           m.name = request.POST['name']
           m.phone = request.POST['userphone']
           m.email = request.POST['useremail']
           m.username = request.user
           m.save()
       return redirect('zeronine:mypage_list')

   else:
       memberForm = MemberForm
       return render(request, 'mypage/mypage_list.html', {'memberForm':memberForm, 'member':member, 'current_category': current_category, 'categories': categories})


def profile_delete_view(request):
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, '회원탈퇴가 완료되었습니다.')
            return redirect('zeronine:mypage_list')

    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'mypage/profile_delete.html', {'password_form': password_form, 'member':member, 'current_category': current_category, 'categories': categories})

@login_required
def password_edit_view(request):
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()

    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)

        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)

            return redirect('zeronine:mypage_list')

    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'mypage/mypage_pwchange.html', {'password_change_form': password_change_form, 'member':member, 'current_category': current_category, 'categories': categories})


def mypage_joinlist(request):
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()
    join_objects = Join.objects.all()
    join_detail_objects = JoinDetail.objects.all()
    products = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    element_object = Element.objects.all()
    value_object = Value.objects.all()

    return render(request, 'mypage/mypage_joinlist.html', {'member':member,
                                                           'join_objects':join_objects,
                                                           'join_detail_objects': join_detail_objects,
                                                           'current_category': current_category,
                                                           'categories': categories,
                                                           'designated_object': designated_object,
                                                           'element_object': element_object,
                                                           'value_object': value_object,
                                                           'products': products})

def mypage_zzimlist(request):
    zzim = Zzim.objects.all()
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()
    join_objects = Join.objects.all()
    join_detail_objects = JoinDetail.objects.all()
    products = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    element_object = Element.objects.all()
    value_object = Value.objects.all()

    return render(request, 'mypage/mypage_zzimlist.html', {'member':member,
                                                           'join':join_objects,
                                                           'join_detail': join_detail_objects,
                                                           'current_category': current_category,
                                                           'categories': categories,
                                                           'designated_object': designated_object,
                                                           'element_object': element_object,
                                                           'value_object': value_object,
                                                           'products': products,
                                                           'zzim':zzim,})

def zzim_delete(request, pk):
    zzim = Zzim.objects.get(pk=pk)
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()
    join_objects = Join.objects.all()
    join_detail_objects = JoinDetail.objects.all()
    products = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    element_object = Element.objects.all()
    value_object = Value.objects.all()

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == 'POST':
        zzim.delete()
        return redirect('zeronine:mypage_zzimlist')

    return render(request, 'mypage/mypage_zzimlist.html', {'zzim': zzim,
                                                           'categories': categories,
                                                           'member': member,
                                                           'join': join_objects,
                                                           'join_detail': join_detail_objects,
                                                           'current_category': current_category,
                                                           'designated_object': designated_object,
                                                           'element_object': element_object,
                                                           'value_object': value_object,
                                                           'products': products,
                                                           'zzim': zzim,
                                                           })

def mypage_uploadlist(request):
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()
    join_object = Join.objects.all()
    join_detail_objects = JoinDetail.objects.all()
    product_object = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    element_object = Element.objects.all()
    value_object = Value.objects.all()

    return render(request, 'mypage/mypage_uploadlist.html', {'member': member,
                                                             'join_object': join_object,
                                                             'join_detail_objects': join_detail_objects,
                                                             'current_category': current_category,
                                                             'categories': categories,
                                                             'designated_object': designated_object,
                                                             'element_object': element_object,
                                                             'value_object': value_object,
                                                             'product_object': product_object})

def mypage_delete(request, pk):
    product = Product.objects.get(pk=pk)
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()
    join_object = Join.objects.all()
    join_detail_objects = JoinDetail.objects.all()
    product_object = Product.objects.all()
    designated_object = Designated.objects.filter(rep_price='True')
    element_object = Element.objects.all()
    value_object = Value.objects.all()

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == 'POST':
        product.delete()
        return redirect('zeronine:mypage_uploadlist')

    return render(request, 'mypage/mypage_uploadlist.html', {'member': member,
                                                             'join_object': join_object,
                                                             'join_detail_objects': join_detail_objects,
                                                             'current_category': current_category,
                                                             'categories': categories,
                                                             'designated_object': designated_object,
                                                             'element_object': element_object,
                                                             'value_object': value_object,
                                                             'product_object': product_object,
                                                             'product':product,
                                                             })