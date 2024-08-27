from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,\
                                            PageNotAnInteger

def post_list(request):
    object_list = Post.published.all()
    paginator   = Paginator(object_list,3) # 3 posts in  each page
    page        = request.GET.get('page')
    try:
        posts    = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts    = paginator(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts    = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page':page,
                   'post': posts})