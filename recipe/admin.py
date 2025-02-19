from django.contrib import admin
from .models import Recipe, Comment
from django.contrib.auth.models import User
from django.utils.html import format_html


# Unregister the default User admin
admin.site.unregister(User)


# Create a custom UserAdmin
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")  # Add "id"


# Register the custom UserAdmin
admin.site.register(User, UserAdmin)

# Register RecipeAdmin
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('approved', 'title', 'slug', 'featured_image', 'status', 'author', 'created_on')
    list_display_links = ('approved', 'title', 'slug')  # Fields that are clickable
    prepopulated_fields = {'slug': ('title',)}  # Auto-fills slug from title


# Add bulk approve function to Comment section of Admin
@admin.action(description='Approve selected comments')
def approve_comments(modeladmin, request, queryset):
    updated = queryset.update(approved=True)
    modeladmin.message_user(request, f'{updated} comment(s) successfully approved.')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('approved', 'body', 'recipe', 'author', 'created_on')
    list_display_links = ('approved', 'body', 'recipe')  # Fields that are clickable
    actions = [approve_comments]


# Register the Comment model
admin.site.register(Comment, CommentAdmin)


