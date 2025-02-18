from django import forms
from .models import Recipe
from .models import Comment


class RecipeForm(forms.ModelForm):
    # Define the fields in the class body, not inside the Meta class
    title = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={'placeholder': 'Recipe Title'})
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Provide a detailed description of your recipe'})
    )
    
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'List all ingredients with amounts and units here'})
    )
    
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Provide detailed instructions for your recipe'})
    )

    class Meta:
        model = Recipe
        fields = ["title", "featured_image", "description", "ingredients", "instructions", "servings", "status"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)