from django.shortcuts import render, redirect

from account.models import Account
from account.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home_screen(request):
    context = {}

    accounts = Account.objects.all()
    print(accounts)
    context['accounts'] = accounts
    return render(request,'home.html',context)

def registration_View(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password1=raw_password)
            login(request, account)
            return redirect(home_screen)
        else:
            context['form'] = form 
    else:
        form = RegistrationForm()
        context['form'] = form 
    return render(request,'register.html', context)

def logout_view(request):
    logout(request)
    return redirect(home_screen)

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect(home_screen)

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect(home_screen)

    else:
        form = AccountAuthenticationForm()
        context['form'] = form
    return render(request,'login.html',context)

