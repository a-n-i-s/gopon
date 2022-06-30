from urllib.request import Request
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'secret/home.html')
