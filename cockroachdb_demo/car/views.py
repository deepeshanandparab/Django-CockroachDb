from django.shortcuts import render

def homePage(request):
    return render(request, 'car/home.html')