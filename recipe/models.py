from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


def validate_not_empty(value):
    """Ensures that the field is not empty or just whitespace."""
    if not value.strip():
        raise ValidationError("This field cannot be empty.")


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    featured_image = CloudinaryField('image', folder="recipes/", format="jpg", unique_filename=False, default="placeholder")
    description = models.TextField(blank=False, validators=[validate_not_empty])
    ingredients = models.TextField(blank=False, validators=[validate_not_empty])
    instructions = models.TextField(blank=False, validators=[validate_not_empty])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    servings = models.PositiveSmallIntegerField(blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        # Ensuring title uniqueness and generating a unique title if not provided
        if not self.title:
            base_title = "Recipe Title"
            counter = 1
            new_title = base_title
            while Recipe.objects.filter(title=new_title).exists():
                counter += 1
                new_title = f"{base_title} {counter}"
            self.title = new_title
        
        # Generating the slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"