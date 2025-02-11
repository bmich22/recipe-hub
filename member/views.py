from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm


def member_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)  # Authenticate the user
            if user is not None:
                login(request, user)  # ✅ Log in the user
                return redirect("recipe:member-home")  # ✅ Redirect after login
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
            return redirect("member:member_login")
    else:
        # if form is not submitted
        form = UserRegistrationForm()
    # validation message or empty form in the case that form was not submitted
    return render(request, "member/register.html", {"form": form})


def member_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("member:member_login")