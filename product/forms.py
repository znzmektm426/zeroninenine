from django import forms
from django.forms import NumberInput

from zeronine.models import *

class ProductForm(forms.Form):
    name = forms.CharField(error_messages={'required': "상품명을 입력하세요."}, max_length=32, label="상품명")
    benefit = forms.CharField(error_messages={'required': "공동구매 취지를 입력해주세요."}, label="공동구매 취지", widget=forms.Textarea)
    detail = forms.CharField(error_messages={'required': "상품 설명을 입력하세요"}, label="상품 설명")
    target_price = forms.IntegerField(error_messages={'required': "목표 금액을 입력하세요."}, label="목표금액")
    photo = forms.ImageField(error_messages={'required': "상세 이미지를 첨부해주세요."}, label="상세이미지")
    start_date = forms.DateField(error_messages={'required': "모집 시작일을 선택해주세요."}, label="모집 시작일", widget=NumberInput(attrs={'type': 'date'}))
    due_date = forms.DateField(error_messages={'required': "모집 마감일을 선택해주세요."}, label="모집 마감일", widget=NumberInput(attrs={'type': 'date'}))
    category_code = forms.ModelChoiceField(error_messages={'required': "카테고리를 선택해주세요."}, label="카테고리", queryset=Category.objects.all())
    kakao_link = forms.CharField(error_messages={'required': "채팅방 링크를 입력하세요."}, max_length=100, label="카카오톡 링크")

class PhotoForm(forms.Form):
    image = forms.ImageField(error_messages={'required': "상세 이미지를 첨부해주세요."}, label="상세이미지")

class OptionForm(forms.Form):
    option_name = forms.CharField(error_messages={'required': "옵션명을 입력하세요."}, max_length=32, label="옵션명")
    # second_option_name = forms.CharField(error_messages={'required': "옵션명을 입력하세요."}, max_length=32, label="옵션명")

class ValueForm(forms.Form):
    value_name = forms.CharField(error_messages={'required': "옵션값을 입력하세요."}, max_length=32, label="옵션명")
    second_value = forms.CharField(error_messages={'required': "옵션값을 입력하세요."}, max_length=32, label="옵션명")
    third_value = forms.CharField(error_messages={'required': "옵션값을 입력하세요."}, max_length=32, label="옵션명")
    option_price = forms.IntegerField(error_messages={'required': "옵션명을 입력하세요."}, label="옵션추가비용")
    second_option_price = forms.IntegerField(error_messages={'required': "옵션명을 입력하세요."}, label="옵션추가비용")
    third_option_price = forms.IntegerField(error_messages={'required': "옵션명을 입력하세요."}, label="옵션추가비용")

class DesignatedForm(forms.Form):
    price = forms.IntegerField(error_messages={'required': "옵션명을 입력하세요."}, label="가격")
