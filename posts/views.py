from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post

# Create your views here.
def home_page(request):
    posts = Post.objects.all()

    #return HttpResponse('<html><title>blog</title></html>')
    return render(request, 'home.html', {'posts': posts})

def api_page(request):
    return render(request, 'api_home.html')

def posts_api_page(request):
    #return HttpResponse('<html>None</html>')
    return HttpResponse('None')
