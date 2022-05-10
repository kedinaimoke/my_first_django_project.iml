from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import Comment
from .forms import CommentForm


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'janes_blog/index.html', {'posts': posts})


# def post_details(request):
#     return render(request, 'janes_blog/blog_detail_page.html', {})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_comment = Comment(post=post, text=text)
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'janes_blog/blog_detail_page.html', context)
