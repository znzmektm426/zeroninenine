from django import forms

from zeronine.models import *

class ElementForm(forms.Form):
    value_code2 = forms.ModelChoiceField(error_messages={'required': "옵션을 선택하세요."}, label="옵션", queryset=Value.objects.all())

class JoinDetailForm(forms.Form):
    quantity = forms.IntegerField(error_messages={'required': "1개 이상 선택 시 참여가 가능합니다."}, label="수량")
    price2 = forms.IntegerField(error_messages={'required': "1개 이상 선택 시 참여가 가능합니다."}, label="가격")
    value_code2 = forms.ModelChoiceField(error_messages={'required': "옵션을 선택하세요."}, label="옵션", queryset=Value.objects.all())