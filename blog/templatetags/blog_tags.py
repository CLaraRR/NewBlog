from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_post(num = 1):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_most_read_posts(num = 5):
    return Post.objects.all().order_by('-views')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order = 'DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts = Count('post')).filter(num_posts__gt = 0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts = Count('post')).filter(num_posts__gt = 0)
