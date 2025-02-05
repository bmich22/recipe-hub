from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    # if the form has been submitted
    if request.method == "POST":
        # then form is submitted with information
        form = UserCreationForm(request.POST)
        # information is validated
        if form.is_valid():
            # information about new user is saved
            form.save()
            # send user back to recipe list page
            return redirect("recipe:list")
    else:
        # if form is not submitted
        form = UserCreationForm()
    # validation message or empty form in the case that form was not submitted
    return render(request, "member/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login here
            return redirect("recipe:list")
    else:
        form = AuthenticationForm()
    return render(request, "member/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/recipes/")