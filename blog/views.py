from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def hello(request):
	return HttpResponse('hello world')

def hello_with_template(request):
	return render(request, 'hello.html')

def list_posts(request):
	all_posts = Post.objects.all()
	return render(request, 'list_posts.html', {
		'posts':all_posts,
	})
