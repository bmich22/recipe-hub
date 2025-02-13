from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, default="Recipe Title")

    def save(self, *args, **kwargs):
        if not self.title:
            base_title = "Recipe Title"
            counter = 1
            new_title = base_title
            while Recipe.objects.filter(title=new_title).exists():
                counter += 1
                new_title = f"{base_title} {counter}"
            self.title = new_title
        super().save(*args, **kwargs)
        
    description = models.TextField(blank=False, default="You must enter a description here.")
    ingredients = models.TextField(blank=False, default="Enter your ingredients with amounts and units here.")
    instructions = models.TextField(blank=False, default="Enter your instructions here.")
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