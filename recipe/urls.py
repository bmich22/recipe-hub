from django.urls import path
from . import views
from .views import add_recipe
from .views import member_recipes

app_name = "recipe"

urlpatterns = [
    path('search/', views.recipe_search, name='recipe_search'),
    path('', views.RecipeList.as_view(), name="list"),
    path('add_recipe/', views.add_recipe, name="addrecipe"),
    path("member_recipes/", member_recipes, name="member_recipes"),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit/', views.edit_recipe, name='edit_recipe'),
    path('<slug:slug>/delete/', views.delete_recipe, name='delete_recipe'),
]