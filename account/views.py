from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignupForm, SigninForm


# Create your views here.
def index(request):
    return render(request, 'account/index.html')


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('account:index')
    if request.method == "POST":
        form = SigninForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                if request.user.is_authenticated:
                    return redirect('account:index')
    else:
        form = SigninForm()
    return render(request, 'account/sign_in.html', {
        'form': form,
    })


def sign_out(request):
    logout(request)
    return redirect('account:index')


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('account:index')
    else:
        form = SignupForm()
    return render(request, 'account/sign_up.html', {
        'form': form,
    })
