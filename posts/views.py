from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post

# Create your views here.
def home_page(request):
    posts = Post.objects.all()

    #return HttpResponse('<html><title>blog</title></html>')
    return render(request, 'home.html', {'posts': posts})

def api_page(request):
    return render(request, 'api_home.html')

def posts_api_page(request):
    if request.method == 'POST':
        title_text = request.POST['title_text']
        content_text = request.POST['content_text']
        post_ = Post.objects.create(title=title_text, content=content_text)

        return redirect(f'/api/posts/{post_.id}')

    posts = str(list(Post.objects.all().values()))

    return HttpResponse(posts)

def posts_api_list_page(request, list_id):
    if request.method == 'DELETE':
        Post.objects.filter(id=list_id).delete()

    if request.method == 'PUT':
        try:
            Post.objects.get(id=list_id)
            post_ = Post.objects.filter(id=list_id)
            put_request = eval(request.body.decode('utf-8'))
            title_text = put_request['title_text']
            content_text = put_request['content_text']
            post_.update(title=title_text,
                         content=content_text)
        except ObjectDoesNotExist:
            put_request = eval(request.body.decode('utf-8'))
            title_text = put_request['title_text']
            content_text = put_request['content_text']
            Post.objects.create(title=title_text,
                                content=content_text)

    if request.method == 'PATCH':
        try:
            Post.objects.get(id=list_id)
            post_ = Post.objects.filter(id=list_id)
            patch_request = eval(request.body.decode('utf-8'))
            try:
                title_text = patch_request['title_text']
                Post.objects.update(title=title_text)
            except KeyError:
                pass

            try:
                content_text = patch_request['content_text']
                Post.objects.update(content=content_text)
            except KeyError:
                pass

        except ObjectDoesNotExist:
            patch_request = eval(request.body.decode('utf-8'))
            title_text = patch_request['title_text']
            content_text = patch_request['content_text']
            Post.objects.create(title=title_text,
                                content=content_text)

    post_ = str(list(Post.objects.filter(id=list_id).values()))
    return HttpResponse(post_)

