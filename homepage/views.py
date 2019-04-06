from django.shortcuts import render

# Create your views here.

def homepage_home(request):
    return render(request, "homepage_home.html", {})
