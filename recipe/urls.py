from django.urls import path
from django.views import generic
from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.RecipeList, name="list"),
    path('add_recipe/', views.add_recipe, name="addrecipe"),
]