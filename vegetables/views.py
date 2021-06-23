from django.shortcuts import render

def home(request):
    return render(request, 'vegetables/home.html')

def shopping(request):
    return render(request, 'vegetables/shopping.html')
