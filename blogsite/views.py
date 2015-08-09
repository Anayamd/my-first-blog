from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

from django.utils import timezone
from .models import Post
from .forms import PostForm, UserCreateForm, CommentForm

# Create your views here.
def post(request):
	return redirect('blogsite.views.post_list')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blogsite/post_list.html', {'posts' : posts})

@login_required
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('blogsite.views.post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'blogsite/post_detail.html', {'post' : post, 'form' : form})

@login_required
def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			if request.FILES:
				post.docfile = request.FILES['docfile']
			post.save()
			return redirect('blogsite.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blogsite/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			if request.FILES:
				post.docfile = request.FILES['docfile']
			post.save()
			return redirect('blogsite.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blogsite/post_edit.html', {'form' : form})

@login_required
def post_tags(request, tag):
	posts = Post.objects.filter(tags=tag).order_by('-published_date')
	if len(posts) == 0:
		return redirect('blogsite.views.post_list')
	return render(request, 'blogsite/post_search.html', {'posts' : posts, 'search' : '<'+tag+'>'})

@login_required
def post_author(request, user):
	posts = Post.objects.filter(author__username=user).order_by('-published_date')
	if len(posts) == 0:
		return redirect('blogsite.views.post_list')
	return render(request, 'blogsite/post_search.html', {'posts' : posts, 'search' : user})

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('blogsite.views.post_list')

def register(request):
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return redirect('django.contrib.auth.views.login')
	else:
		form = UserCreateForm()
	return render(request, 'registration/register.html', {'form' : form})