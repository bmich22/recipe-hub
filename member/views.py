from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# def member(request):
#     template = loader.get_template('register.html')
#     return HttpResponse(template.render())

# def register_view(request):
#     return render(request, "member/register.html")


def register_view(request):
    template = loader.get_template('member/register.html')
    return HttpResponse(template.render())
