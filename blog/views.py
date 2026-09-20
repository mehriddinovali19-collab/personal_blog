from django.shortcuts import (render, get_object_or_404, redirect)
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        published=True,
    )
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=post.slug)

    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/form.html",
        {"form": form}
    )
