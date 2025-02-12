from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import RecipeForm, IngredientFormSet
from .models import Recipe, Ingredient


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    # template_name = "recipe/index.html"
    paginate_by = 6
    
    def get_template_names(self):
        """Dynamically choose a template based on a condition."""
        if self.request.user.is_authenticated:
            return ["recipe/member_home.html"]  # Template for logged-in users
        else:
            return ["recipe/index.html"]  # Template for guests
        

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