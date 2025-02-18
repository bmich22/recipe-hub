from django.test import TestCase
from .forms import RecipeForm


# Create your tests here.
class TestRecipeForm(TestCase):

    def test_form_is_valid(self):
        recipe_form = RecipeForm({'title': 'Penne Arribiata', 'description': 'spicy pasta', 'ingredients': 'pasta', 'instructions': 'First you do this.', 'servings': 4, 'status': 1})
        self.assertTrue(recipe_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        recipe_form = RecipeForm({'title': '', 'description': 'spicy pasta', 'ingredients': 'pasta', 'instructions': 'do this.', 'servings': 4, 'status': 1})
        self.assertFalse(recipe_form.is_valid(), msg='Form is valid')    
    