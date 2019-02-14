from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.RegexField(label="아이디",
                                max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="아이디를 입력해주세요")
    email = forms.EmailField(label="이메일",
                             required=True,
                             help_text="이메일을 입력해주세요")
    name = forms.CharField(max_length=10,
                           label="이름",
                           help_text="이름을 입력해주세요")
    password1 = forms.CharField(label="비밀번호",
                                help_text="비밀번호를 입력해주세요",
                                widget=forms.PasswordInput
                                )
    password2 = forms.CharField(label="비밀번호",
                                help_text="비밀번호를 입력해주세요",
                                widget=forms.PasswordInput
                                )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'email')
