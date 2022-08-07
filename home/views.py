from django.shortcuts import render, redirect


# Create your views here.
def mainHome(request):
    return render(request, "home/index.html")
