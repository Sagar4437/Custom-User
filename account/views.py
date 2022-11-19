from django.shortcuts import render, redirect

from account.models import Account

# Create your views here.

def home_screen(request):
    context = {}

    accounts = Account.objects.all()
    print(accounts)
    context['accounts'] = accounts
    return render(request,'home.html',context)