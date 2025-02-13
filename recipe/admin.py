from django.contrib import admin
from .models import Recipe
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")  # Add "id" here


# Register RecipeAdmin with the inline Ingredient form
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}  # Auto-fills slug from title


