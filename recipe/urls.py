from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.RecipeList.as_view(), name="list"),
    path('member_home', views.RecipeList.as_view(), name="member-home"),
    path('add_recipe/', views.add_recipe, name="addrecipe"),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]