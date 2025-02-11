from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/main_before_registration.html')

def about(request):
    return render(request, 'main/about.html')

def registration(request):
    return render(request, 'main/registration.html')