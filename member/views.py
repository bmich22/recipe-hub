from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe:list")
    else:
        form = UserCreationForm
    form = UserCreationForm()
    return render(request, "member/register.html", {"form": form})
