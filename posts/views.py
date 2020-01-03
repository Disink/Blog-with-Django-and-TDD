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
    print(request)
    if request.method == 'POST':
        title_text = request.POST['title_text']
        content_text = request.POST['content_text']
        Post.objects.create(title=title_text, content=content_text)

    posts = str(list(Post.objects.all().values()))

    return HttpResponse(posts)
