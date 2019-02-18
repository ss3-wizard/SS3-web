from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignupForm


# Create your views here.
def index(request):
    return render(request, 'account/index.html')


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('account:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
    else:
        form = AuthenticationForm()
    return render(request, 'account/sign_in.html', {
        'form': form
    })


def sign_out(request):
    logout(request)
    return redirect('account:index')


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:index')
    else:
        form = SignupForm()
        # form = UserCreationForm()
    return render(request, 'account/sign_up.html', {
        'form': form,
    })
