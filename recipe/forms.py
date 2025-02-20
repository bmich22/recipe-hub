from django import forms
from .models import Recipe, STATUS
from .models import Comment


class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={'placeholder': 'Recipe Title, max 50 characters'})
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

    status = forms.ChoiceField(
        choices=STATUS,  # Use the STATUS choices from the model
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 100px; border-radius: 0px; border-color: black; line-height: 1.0rem;'}),
        label="Status: Choose 'Draft' to save your recipe so you can finish it later or 'Published' to show it is ready for approval."
    )

    class Meta:
        model = Recipe
        fields = ["title", "featured_image", "description", "ingredients", "instructions", "servings", "status"]


class CommentForm(forms.ModelForm):
    # Assign form class 'form-control'to make text area responsive
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here.'}),
        label=False  # This removes the label entirely
    )

    class Meta:
        model = Comment
        fields = ('body',)