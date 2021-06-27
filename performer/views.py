from django.shortcuts import render

# Create your views here.
def performer(request):
    return render(request, 'performer/performer.html')

def performers(request):
    return render(request, 'performer/performers.html')