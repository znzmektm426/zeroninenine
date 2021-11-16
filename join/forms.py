from django import forms

from zeronine.models import *

class ElementForm(forms.Form):
    value_code2 = forms.ModelChoiceField(error_messages={'required': "옵션을 선택하세요."}, label="옵션", queryset=Value.objects.all())

class JoinDetailForm(forms.Form):
    quantity = forms.IntegerField(error_messages={'required': "1개 이상 선택 시 참여가 가능합니다."}, label="수량")
    price2 = forms.IntegerField(error_messages={'required': "1개 이상 선택 시 참여가 가능합니다."}, label="가격")
    value_code2 = forms.ModelChoiceField(error_messages={'required': "옵션을 선택하세요."}, label="옵션", queryset=Value.objects.all())
    name = forms.CharField(error_messages = {'required':"주문자명을 입력해주세요."}, label = "주문자명", max_length=64)
    phone = forms.CharField(error_messages = {'required':"전화번호를 입력해주세요."}, label = "전화번호", max_length=64)
    address = forms.CharField(error_messages = {'required':"도로명 주소를 입력해주세요."}, label = "도로명 주소", max_length=300)
    address2 = forms.CharField(error_messages={'required': "상세주소를 입력해주세요."}, label="상세주소를", max_length=300)