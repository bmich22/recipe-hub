from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import RecipeForm
from .forms import CommentForm


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1, approved=True).order_by('-created_on')
    template_name = "recipe/index.html"
    paginate_by = 4
    

def recipe_detail(request, slug):
    """
    Display an individual recipe
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.'
            )

    comment_form = CommentForm()

    return render(
        request, 
        "recipe/recipe_detail.html", 
        {
            "recipe": recipe, 
            "comments": comments, 
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

        
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)  # Don't save yet
            recipe.author = request.user  # Assign the logged-in user
            recipe.save()  # Now save it
            messages.add_message(
                request, messages.SUCCESS,
                'Success! You recipe has been submitted and is awaiting approval')
            return redirect("recipe:list")  # Redirect to the recipe list page

    else:
        form = RecipeForm()

    return render(request, "recipe/add_recipe.html", {
        "form": form,
    })


@login_required
def member_recipes(request):
    member_list = Recipe.objects.filter(author=request.user)  # Get recipes for logged-in user
    return render(request, "recipe/member_recipes.html", {"member_list": member_list})


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Ensure that the logged in user is the owner of the recipe
    if request.user != recipe.author:
        messages.error(request, "You are not authorized to edit this recipe.")
        return redirect("recipe:recipe_detail", recipe.slug)
        # return redirect("recipe:recipe_detail", slug=recipe.slug)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():	
            form.save()
            messages.success(request, "Recipe updated successfully")
            return redirect("recipe:recipe_detail", recipe.slug)
            # return redirect("recipe:recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
        return render(request, "recipe/edit_recipe.html", {"form": form, "recipe": recipe})

@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    # Ensure the logged-in user is the author of the recipe
    if request.user != recipe.author:
        messages.error(request, "You are not authorized to delete this recipe.")
        return redirect("recipe:recipe_detail", slug=recipe.slug)

    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("recipe:list")

    return render(request, "recipe/delete_recipe.html", {"recipe": recipe})


def recipe_search(request):
    query = request.GET.get('query', '')  # Get the search query from the URL parameter
    recipes = Recipe.objects.filter(status=1)

    if query:
        recipes = recipes.filter(ingredients__icontains=query)  # Filter recipes by the query
    return render(request, 'recipe/recipe_search.html', {
        'query': query,
        'recipes': recipes
    })

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated and waiting approval.')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe:recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe:recipe_detail', args=[slug]))