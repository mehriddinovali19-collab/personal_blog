from django.shortcuts import (render, get_object_or_404, redirect)
from .models import Post, Category
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.filter(
        published=True
    ).order_by('-created_at')

    categories = Category.objects.all()

    return render(
        request,
        'blog/home.html',
        {
            'posts': posts,
            'categories': categories,
        }
    )



def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render( request, 'blog/post_list.html', { 'page_obj': page_obj, 'posts': page_obj, } )

def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        published=True,
    )
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required

def post_create(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('post_detail', slug=post.slug)

    else:

        form = PostForm()

    return render(
        request,
        'blog/form.html',
        {'form': form}
    )

@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect("post_detail", slug=post.slug)

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

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if post.authotr != request.user:
        return redirect("post_detail", slug=post.slug)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form, "post": post})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)

    posts = Post.objects.filter(
        category=category,
        published=True
    ).order_by('-created_at')

    return render(
        request,
        'blog/category_posts.html',
        {
            'category': category,
            'posts': posts,
        }
    )

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        title__icontains=query,
        published=True
    ).order_by('-created_at') if query else []
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


