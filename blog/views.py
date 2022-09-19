from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from tags.models import Tag
from .forms import CommentForm, PostForm
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


# Create your views here.
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.images = request.FILES.get('images')
            post.save()
            return redirect('draft')
    else:
        form = PostForm()
    ctx = {
        'form':form,
    }

    return render(request, 'blog/new_post.html', ctx)
    
def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    recent_post = Post.objects.filter(published=True).order_by('-id')[0:3]
    context = {
        'post': post,
        'recent':recent_post,
    }
    return render(request, 'blog/single_post.html',context)

def post_list(request, tag_slug=None):
    tag = None
    post = None

    if tag_slug != None:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post = Post.objects.all().filter(published=True, tag=tag)
        paginator = Paginator(post, 6)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)
    else:
        post = Post.objects.all().filter(published=True).order_by('-created_date')
        paginator = Paginator(post, 6)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)
    
    recent_post = Post.objects.filter(published=True).order_by('-id')[0:3]
    context = {
        'posts':paged_post,
        'recent':recent_post,
    }
    return render(request, 'blog/post_list.html', context)

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.username = form.cleaned_data['username']
            data.text = form.cleaned_data['text']
            data.post = post
            data.save()
            return redirect('post_list')
    else:
        form = CommentForm()

def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.post.pk
    comment.delete()
    return redirect('post_list')


def post_publish(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.publish()
    return redirect('post_list')  


def draft(request):
    post = Post.objects.filter(published=False)
    ctx = {
        'posts':post,
    }
    return render(request, 'blog/draft.html', ctx)

def draft_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    ctx = {
        'post':post,
    }
    return render(request, 'blog/draft_detail.html', ctx)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')







            