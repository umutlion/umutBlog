from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin, CreateView
from .forms import CreateCommentForm

from .models import Post, PostImage, Category, Comment


# Create your views here.


def index(request):
    allPosts = Post.objects.all()
    category = Category.objects.all()
    return render(request, "posts/index.html", {'posts': allPosts,
                                                'allCategories':category})


class PostDetail(DetailView):
    template_name = "posts/index.html"
    model = Post
    context_object_name = "single"
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['allCategories'] = Category.objects.all()
        context['posts']=Post.objects.all()

        return context



def single(request, slug):
    post = get_object_or_404(Post, slug=slug)
    photos = PostImage.objects.filter(post=post)
    return render(request, "posts/single.html", {'single': post,
                                                 'photos':photos})


class CategoryDetail(DetailView):
    model = Category
    template_name = "categories/detail.html"
    context_object_name =  "category"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail,self).get_context_data(**kwargs)
        context["allCategories"] = Category.objects.all()
        return context
