from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password

class MemberForm(forms.Form):
    name = forms.CharField(error_messages = {'required':"아이디 입력해주세요."}, label = "아이디", max_length=128)
    password = forms.CharField(error_messages = {'required':"비밀번호를 입력해주세요."}, label = "비밀번호", widget = forms.Textarea)
    email = forms.EmailField(error_messages = {'required':"이메일을 입력해주세요."}, label = "이메일", max_length=128)
    phone = forms.CharField(error_messages = {'required':"전화번호를 입력해주세요."}, label = "전화번호", max_length=64)

class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '현재 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })
