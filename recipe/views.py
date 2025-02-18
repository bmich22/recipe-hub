from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1, approved=True).order_by('-created_on')
    template_name = "recipe/index.html"
    paginate_by = 4
    

def recipe_detail(request, slug):
    """
    Display an individual recipe
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    return render(request, "recipe/recipe_detail.html", {"recipe": recipe},)

        
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)  # Don't save yet
            recipe.author = request.user  # Assign the logged-in user
            recipe.save()  # Now save it
            messages.add_message(
                request, messages.SUCCESS,
                'Success! You recipe has been submitted and is awaiting approval')
            return redirect("recipe:list")  # Redirect to the recipe list page

    else:
        form = RecipeForm()

    return render(request, "recipe/add_recipe.html", {
        "form": form,
    })


@login_required
def member_recipes(request):
    member_list = Recipe.objects.filter(author=request.user)  # Get recipes for logged-in user
    return render(request, "recipe/member_recipes.html", {"member_list": member_list})


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Ensure that the logged in user is the owner of the recipe
    if request.user != recipe.author:
        messages.error(request, "You are not authorized to edit this recipe.")
        return redirect("recipe:recipe_detail", recipe.slug)
        # return redirect("recipe:recipe_detail", slug=recipe.slug)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():	
            form.save()
            messages.success(request, "Recipe updated successfully")
            return redirect("recipe:recipe_detail", recipe.slug)
            # return redirect("recipe:recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
        return render(request, "recipe/edit_recipe.html", {"form": form, "recipe": recipe})

@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    # Ensure the logged-in user is the author of the recipe
    if request.user != recipe.author:
        messages.error(request, "You are not authorized to delete this recipe.")
        return redirect("recipe:recipe_detail", slug=recipe.slug)

    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("recipe:list")

    return render(request, "recipe/delete_recipe.html", {"recipe": recipe})


def recipe_search(request):
    query = request.GET.get('query', '')  # Get the search query from the URL parameter
    recipes = Recipe.objects.filter(status=1)

    if query:
        recipes = recipes.filter(ingredients__icontains=query)  # Filter recipes by the query
    return render(request, 'recipe/recipe_search.html', {
        'query': query,
        'recipes': recipes
    })