<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from .models import ShopUser
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from django.db import transaction
from .utils import send_verify_mail
=======
from django.shortcuts import render, HttpResponseRedirect
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse
>>>>>>> acd770417932e8546621d2347c271fd85985426b

def login(request):
    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)  
<<<<<<< HEAD
        
=======
>>>>>>> acd770417932e8546621d2347c271fd85985426b
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
        
<<<<<<< HEAD
            user = auth.authenticate(request, username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if "next" in request.GET.keys():
                    return HttpResponseRedirect(request.GET["next"])
=======
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
>>>>>>> acd770417932e8546621d2347c271fd85985426b
                return HttpResponseRedirect(reverse('main'))
    else:
        login_form = ShopUserLoginForm()

    return render(request, 'authapp/login.html', context={
        'title': 'Вход',
<<<<<<< HEAD
        'form': login_form,
    },)
=======
        'form': login_form
    })
>>>>>>> acd770417932e8546621d2347c271fd85985426b

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))   


def register(request):
    if request.method == 'POST':
<<<<<<< HEAD
        register_form = ShopUserRegisterForm(request.POST, request.FILES)      
        if register_form.is_valid():
            user = register_form.save()
            send_verify_mail(user)
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()


    return render(request, 'authapp/register.html', context={
        'title': 'Регистрация',
        'form': register_form,
    },)


@transaction.atomic
def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.profile)      
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.profile)


    return render(request, 'authapp/edit.html', context={
        'title': 'Редактирование',
        'form': edit_form,
        'profile_form': profile_form,
    },)


def verify(request, email, activation_key):
    user = get_object_or_404(ShopUser, email=email)
    if user.activation_key == activation_key:
        user.is_active = True
        user.save()
        auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
    return render(request, 'authapp/verification.html')

=======
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
>>>>>>> acd770417932e8546621d2347c271fd85985426b
