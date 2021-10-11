from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from post.forms import PostForm, CommentForm
from zeronine.models import Category, Post, Comment

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect

# Create your views here.
def post(request):
    current_category = None
    categories = Category.objects.all()

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    page = request.GET.get('page', '1')
    posts = Post.objects.all().order_by('-register_date')
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    index = posts.number
    max_index = len(paginator.page_range)
    page_size = 5

    start_index = index - page_size if index > page_size else 1

    if index + page_size == max_index:
        end_index = max_index
    else :
        end_index = index + page_size if index <= max_index else max_index

    page_range = list(paginator.page_range[start_index-1:end_index])

    return render(request, 'post/post_list.html', {'posts':posts,
                                                   'page_range':page_range,
                                                   'max_index':max_index,
                                                   'page_size':page_size,
                                                   'current_category': current_category, 'categories': categories})

def post_write(request):
    current_category = None
    categories = Category.objects.all()

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['contents']
            post.username = request.user
            post.save()

            return HttpResponseRedirect(reverse('zeronine:post'))

    else:
        form = PostForm()

    return render(request, 'post/post_write.html', {'form': form, 'current_category': current_category, 'categories': categories})

def post_detail(request, pk):
    current_category = None
    categories = Category.objects.all()

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
        # 게시물의 내용을 찾을 수 없을 때 내는 오류 message.

    comments = Comment.objects.filter(post_code=pk)

    return render(request, 'post/post_detail.html', {'post': post, 'comments': comments, 'current_category': current_category, 'categories': categories})

def search(request):
    current_category = None
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-register_date')

    q = request.POST.get('q', "")

    if q:
        posts = posts.filter(title__icontains=q)
        return render(request, 'post/search.html', {'posts': posts, 'q': q, 'current_category': current_category, 'categories': categories})

    else:
        return render(request, 'post/search.html', {'categories': categories})


def post_modify(request, pk):
    current_category = None
    categories = Category.objects.all()
    post = Post.objects.get(pk=pk)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.username = request.user

        post.save()
        return redirect('zeronine:post')

    else:
        postForm = PostForm
        return render(request, 'post/post_modify.html', {'postForm':postForm, 'post':post, 'current_category': current_category, 'categories': categories})

def post_delete(request, pk):
    current_category = None
    categories = Category.objects.all()
    post = Post.objects.get(pk=pk)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('zeronine:login'))

    if request.method == 'POST':
        post.delete()
        return redirect('zeronine:post')
    return render(request, 'post/post_delete.html', {'Post': post,
                                                     'current_category': current_category, 'categories': categories})

def comment_create(request, article_pk):

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.content = form.cleaned_data['contents']
            comment.username = request.user
            comment.post_code = get_object_or_404(Post, pk=article_pk)
            comment.save()

            return HttpResponseRedirect(reverse('zeronine:post_detail', kwargs={'pk': article_pk}))
    else:
        form = CommentForm()

    return HttpResponseRedirect(reverse('zeronine:post_detail', kwargs={'pk': article_pk}))

def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == "POST":
        comment.delete()

        return HttpResponseRedirect(reverse('zeronine:post_detail', kwargs={'pk': comment.post_code.pk}))

    return HttpResponseRedirect(reverse('zeronine:post_detail', kwargs={'pk': comment.post_code.pk}))