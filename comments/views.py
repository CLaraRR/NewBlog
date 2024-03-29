from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            dict = {'post': post, 'form': form, 'comment_list': comment_list}
            return render(request, 'blog/single.html', dict)
    else:
        return redirect(post)







