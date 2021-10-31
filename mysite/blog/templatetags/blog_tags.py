import markdown

from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from taggit.models import Tag
from ..models import Post
from ..forms import SearchForm


register = template.Library()


@register.simple_tag(name='total_posts')
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def get_all_tags():
    return Tag.objects.all()


# @register.inclusion_tag('blog/empty.html')
# def show_search_form():
#     return mark_safe(SearchForm().as_p())
