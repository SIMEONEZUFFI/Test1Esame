from django.shortcuts import render

__all__:["homepage"]

def home(request):
    return render(request, "home.html")