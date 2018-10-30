from django.shortcuts import render
from .models import Post

#from django.http import HttpResponse

posts = [
        {
                'author': 'RP', 
                'title': 'Blog Post 1', 
                'content': 'First post content', 
                'date_posted': 'Sep 26, 2018'
        }, 
        {
                'author': 'Jane Doe', 
                'title': 'Blog Post 2', 
                'content': 'Second post content', 
                'date_posted': 'Sep 27, 2018'
        }, 
        {
                'author': 'Jon Snow', 
                'title': 'Blog Post 3', 
                'content': 'Third post content', 
                'date_posted': 'Sep 29, 2018'
        }   
    ]


# Create your views here.
def home(request):
    context = {
#            'posts': posts
            'posts': Post.objects.all()
            }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


#def contact(request):
#    return HttpResponse('<h1>Blog Contact</h1>')