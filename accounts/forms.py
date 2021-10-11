from django.contrib.auth.forms import UserCreationForm
from django import forms

from zeronine.models import Member

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label=('이메일'),
        required=True,
        widget=forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': 'True',
                }
        )
    )
    class Meta:
        model = Member
        fields = ['name', 'username', 'phone', 'email']

        def clean_password2(self):

            cd = self.cleaned_data
            if cd['password1']!=cd['password2']:
                raise forms.ValidationError
            return cd['password2']