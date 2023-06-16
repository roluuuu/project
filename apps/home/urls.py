from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.LoginView.as_view(template_name="home/login.html"), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
]
urlpatterns += staticfiles_urlpatterns()
