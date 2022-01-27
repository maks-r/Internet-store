from django.shortcuts import render, HttpResponseRedirect
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)  
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
        
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        login_form = ShopUserLoginForm()

    return render(request, 'authapp/login.html', context={
        'title': 'Вход',
        'form': login_form
    })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))   


def register(request):
    if request.method == 'POST':
        register_form = ShopUserEditForm(request.POST, request.FILES)      
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserEditForm()

    return render(request, 'authapp/register.html', context={
        'title': 'Регистрация',
        'form': register_form
    })



def edit(request):
    if edit.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=request.user)      
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = ShopUserRegisterForm(instance=request.user)

    return render(request, 'authapp/edit.html', context={
        'title': 'Редактирование',
        'form': edit_form
    })