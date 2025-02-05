from django.urls import path
from . import views

app_name = "member"

urlpatterns = [
    path('', views.register_view, name='register'),
]