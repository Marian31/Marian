from django.shortcuts import render


def index(request):
    return render(request, "MainApp/homepage.html")
# Create your views here.
