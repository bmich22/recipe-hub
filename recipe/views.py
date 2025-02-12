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
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)  # Don't save yet
            recipe.author = request.user  # Assign the logged-in user
            recipe.save()  # Now save it
            return redirect("recipe:list")  # Redirect to the recipe list page

    else:
        form = RecipeForm()

    return render(request, "recipe/add_recipe.html", {
        "form": form,
    })
