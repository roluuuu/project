from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


# para el login
from . import forms
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST, data=request.POST)
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "Usuario creado"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})


from django.contrib.auth.views import LogoutView


class LogoutView(LogoutView):
    template_name = "home/logout.html"


class LoginView(LoginView):
    template_name = "home/login.html"
