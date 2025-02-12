from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe/index.html"
    paginate_by = 6
    

def recipe_detail(request, slug):
    """
    Display an individual :model:`recipe.Recipe`.

    **Context**

    ``post``
    An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    return render(request, "recipe/recipe_detail.html", {"recipe": recipe},)

        
def add_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user  # Assign the logged-in user as the author
            recipe.save()

            return redirect("recipe_list")  # Redirect to the recipe list page

    else:
        recipe_form = RecipeForm()

    return render(request, "recipe/add_recipe.html", {
        "recipe_form": recipe_form,
    })