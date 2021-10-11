from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from zeronine.models import *


def register(request):
    current_category = None
    categories = Category.objects.all()
    member = Member.objects.all()

    if request.method == 'POST':
        member_form = RegisterForm(request.POST)
        if member_form.is_valid():
            new_member = member_form.save(commit=False)
            new_member.set_password(member_form.cleaned_data['password2'])
            new_member.save()
            return render(request, 'accounts/register_done.html', {'new_member':new_member,
                                                                   'member':member,
                                                                   'current_category': current_category,
                                                                   'categories': categories})
    else:
        member_form = RegisterForm()


    return render(request, 'accounts/register.html', {'form':member_form})


def ai_check(request):

    return render(request, 'accounts/ai_check.html')

