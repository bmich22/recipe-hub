from django.urls import path
from . import views
from .views import register, member_login, member_logout
from django.contrib.auth import views as auth_views

app_name = "member"

urlpatterns = [
    path('register/', register, name='register'),
    path("login/", member_login, name="member_login"),
    path("logout/", member_logout, name="member_logout"),
]