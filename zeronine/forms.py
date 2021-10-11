from django import forms

from zeronine.models import *

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class DetailForm(forms.Form):
    select_option = forms.ModelChoiceField(error_messages={'required': "옵션을 선택하세요."}, label="옵션", queryset=Value.objects.all())
    designated_code = forms.CharField()