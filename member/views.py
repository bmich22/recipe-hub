from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login here
            return redirect("recipe:member-home")
    else:
        form = AuthenticationForm()
    return render(request, "member/login.html", {"form": form})


def register(request):
    # if the form has been submitted
    if request.method == "POST":
        # then form is submitted with information
        form = UserRegistrationForm(request.POST)
        # information is validated
        if form.is_valid():
            # information about new user is saved
            user = form.save()
            login(request, user)  # Log in the user after registering
            # send user back to recipe list page
            return redirect("recipe:list")
    else:
        # if form is not submitted
        form = UserRegistrationForm()
    # validation message or empty form in the case that form was not submitted
    return render(request, "member/register.html", {"form": form})


def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/recipes/")