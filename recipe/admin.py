from django.contrib import admin
from .models import Recipe
from django.contrib.auth.models import User


# Unregister the default User admin
admin.site.unregister(User)


# Create a custom UserAdmin
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")  # Add "id"


# Register the custom UserAdmin
admin.site.register(User, UserAdmin)

# Register RecipeAdmin with the inline Ingredient form
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('approved', 'title', 'slug', 'featured_image','status', 'author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}  # Auto-fills slug from title