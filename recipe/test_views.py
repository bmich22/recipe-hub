from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import RecipeForm
from .models import Recipe


class TestRecipeViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.recipe = Recipe(title="Recipe Title", author=self.user, slug="recipe-title", description="recipe description", ingredients="recipe ingredients", instructions="recipe instructions", servings=0, status=1)
        self.recipe.save()

    def test_render_recipe_detail_page(self):
        response = self.client.get(reverse('recipe:recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"recipe Title", response.content)
        self.assertIn(b"recipe description", response.content)
        self.assertIn(b"recipe ingredients", response.content)
        self.assertIn(b"recipe instructions", response.content)
        self.assertIn(b"recipe servings", response.content)
        self.assertIn(b"recipe status", response.content)
        