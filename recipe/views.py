from django.shortcuts import render, redirect
from django.views import generic
from .forms import RecipeForm, IngredientFormSet
from .models import Recipe, Ingredient

# Create your views here.
# def my_recipe(request):
#     return HttpResponse("Here is the best recipe of all time!")


# def RecipeList(request):
#     return render(request, 'recipe/recipe_list.html')

class RecipeList(generic.ListView):
    model = Recipe


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        formset = IngredientFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            recipe = form.save()  # Save the Recipe
            ingredients = formset.save(commit=False)  # Get ingredients but don't save yet
            for ingredient in ingredients:
                ingredient.recipe = recipe  # Assign the recipe to each ingredient
                ingredient.save()  # Save each ingredient
            return redirect('recipe_list')  # Redirect to the recipe list page

    else:
        form = RecipeForm()
        formset = IngredientFormSet()

    return render(request, 'recipe/add_recipe.html', {'form': form, 'formset': formset})