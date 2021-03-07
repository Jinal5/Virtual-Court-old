from django.shortcuts import render

def home(request):
    return render(request, 'court/home.html', {'title' : 'Home'} )

def about(request):
    return render(request, 'court/about.html', {'title' : 'About'}) 

# Create your views here.
