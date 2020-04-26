from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
def signup_view(request):
    return render(request,"signup.html")
