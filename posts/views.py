from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    #return HttpResponse('<html><title>blog</title></html>')
    return render(request, 'home.html')
