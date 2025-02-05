from django.shortcuts import render

# Create your views here.
# def my_recipe(request):
#     return HttpResponse("Here is the best recipe of all time!")

def recipe_list(request):
    return render(request, 'recipe/recipe_list.html')