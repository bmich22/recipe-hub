from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'servings', 'status']


# Create an inline formset for Ingredients within Recipe
IngredientFormSet = inlineformset_factory(Recipe, Ingredient, 
                                          fields=['amount', 'unit', 'name'], 
                                          extra=3,  # Number of empty ingredient fields to show
                                          can_delete=True)  # Allow ingredient deletion
