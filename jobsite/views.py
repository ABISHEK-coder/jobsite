from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def social(request):
    return render(request, 'social.html')

def works(request):
    return render(request, 'works.html')

def workdetails(request):
    return render(request, 'workdetails.html')

def chat(request):
    return render(request, 'chat.html')

def notification(request):
    return render(request, 'notification.html')

def profile(request):
    return render(request, 'profile.html')

def post(request):
    return render(request, 'post.html')

def applied(request):
    return render(request, 'applied.html')