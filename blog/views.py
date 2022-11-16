from django.shortcuts import render, get_object_or_404, redirect
from .models import Post # The dot before models means current directory or current application
from django.utils import timezone
from .forms import PostForm


# A view is a place where we put the "logic" of our application. 
# "View" supposed to connect models and templates
# in a "View" we decide what (model) will be displayed in a template
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # 'request' is everything we receive from the user via the Internet.
    # the last parameter {} is a place in which we can add some things for the template to use.

def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context={'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # save the form
            # commit=False means that we don't want to save the Post model yet- we want to add the author first.
            post.author = request.user
            # add author since there was no author field in the PostForm and this field is required.
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    # To create a new Post form, we need to call PostForm() and pass it to the template.
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
       form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

    


