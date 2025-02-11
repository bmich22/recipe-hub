from django.shortcuts import render, redirect
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