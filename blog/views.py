from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.db.models import Q

import markdown


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # paginate_by = 5

class BlogsView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'


class PostPageView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostPageView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostPageView, self).get_object(queryset = None)
        md = markdown.Markdown(extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify = slugify),
        ])
        post.content = md.convert(post.content)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        context = super(PostPageView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list,
        })
        return context


class ArchiveView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(create_time__year = year, create_time__month = month)


class CategoryView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category = cate)


class TagView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk = self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags = tag)


def about_page(request):
    return render(request, 'blog/about.html')


def contact_page(request):
    return render(request, 'blog/contact.html')