from django.shortcuts import render
from .models import Post # The dot before models means current directory or current application
from django.utils import timezone

# A view is a place where we put the "logic" of our application. 
# "View" supposed to connect models and templates
# in a "View" we decide what (model) will be displayed in a template
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # 'request' is everything we receive from the user via the Internet.
    # the last parameter {} is a place in which we can add some things for the template to use.
    
