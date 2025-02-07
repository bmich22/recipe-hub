from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.RecipeList.as_view(), name="list"),
    path('add_recipe/', views.add_recipe, name="addrecipe"),
]