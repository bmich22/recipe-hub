from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "ingredients", "instructions", "servings", "status"]



# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['title', 'author', 'servings', 'status']


# # Create an inline formset for Ingredients within Recipe
# IngredientFormSet = inlineformset_factory(Recipe, Ingredient, 
#                                           fields=['amount', 'unit', 'name'], 
#                                           extra=3,  # Number of empty ingredient fields to show
#                                           can_delete=True)  # Allow ingredient deletion
