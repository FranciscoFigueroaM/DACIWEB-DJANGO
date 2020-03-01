from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def objectives(request):
    return render(request, "core/objectives.html")


def rules(request):
    return render(request, "core/rules.html")
