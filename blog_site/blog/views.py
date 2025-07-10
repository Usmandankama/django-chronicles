from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})
    
    return HttpResponse(output)