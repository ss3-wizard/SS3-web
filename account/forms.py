from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.RegexField(max_length=20,
                                min_length=5,
                                regex=r"^[가-힣a-zA-Z0-9]+$",
                                help_text="아이디를 입력해주세요",
                                error_messages={
                                    'invalid': "5~20자의 영문, 한글, 숫자만 사용 가능합니다"
                                })

    password1 = forms.CharField(max_length=16,
                                min_length=8,
                                help_text="비밀번호",
                                error_messages={
                                    'invalid': '8~16자의 비밀번호를 만들어주세요'
                                },
                                widget=forms.PasswordInput
                                )
    password2 = forms.CharField(help_text="비밀번호 재확인",
                                error_messages={
                                    'invalid': '비밀번호가 일치하지 않습니다'
                                },
                                widget=forms.PasswordInput
                                )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
