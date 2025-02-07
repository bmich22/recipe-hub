from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    servings = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.amount} {self.unit} {self.name}"


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instructions")
    step_number = models.PositiveIntegerField()
    instruction_content = models.TextField()

    def __str__(self):
        return f"{self.step_number} {self.instruction_content}"