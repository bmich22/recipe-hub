from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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
