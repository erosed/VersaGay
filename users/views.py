from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Gasto, calendario
from .forms import NuevoGasto, lista, actualizarform
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
        )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

def custom_login(request):
    if request.user.is_authenticated:
        return redirect("homepage")

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("homepage")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )

def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'users/profile.html', context={'form': form})

    return redirect("homepage")

def NuevoGastoView(request):
	return render(request, 'users/vergastos.html')

def subirgasto(request, username):
    if request.method == "POST":
        user = request.user
        form = NuevoGasto(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("vergastos", user.username)
    else:
        form = NuevoGasto()
        return render(request, "users/nuevogasto.html", {"form":form})
    #return redirect("homepage")


def vergasto(request, username):
	lista_gastos= Gasto.objects.filter(author=request.user.id)
	return render(request, 'users/vergastos.html', {
        'lista_gastos': lista_gastos
    })

def verlink(request, pk):
    enlace = Gasto.objects.get(pk=pk)
    return render(request, 'users/verlink.html', {
        'enlace':enlace
    })

def borrarlink(request, pk,):
    if request.method == "POST":
        user = request.user
        borrar = Gasto.objects.get(pk=pk)
        borrar.delete()
    return redirect("vergastos", user.username)

def userid(request):
    return (request.user.id)