from django.shortcuts import render, redirect
from .forms import RecipeForm

# Create your views here.
# def my_recipe(request):
#     return HttpResponse("Here is the best recipe of all time!")


def recipe_list(request):
    return render(request, 'recipe/recipe_list.html')


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user  # Assign logged-in member
            recipe.save()
            return redirect("recipe:list")  # Redirect to recipe list
    else:
        form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form': form})