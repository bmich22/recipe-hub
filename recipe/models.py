from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    slug = models.SlugField(max_length=200, unique=True)
    instructions = models.TextField()
    servings = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')  # One-to-Many
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.amount} {self.unit} {self.name} (for {self.recipe.title})"
