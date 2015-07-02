from django.shortcuts import render_to_response
 
from FirstBlog.blog.models import posts

 
import datetime

"""
def home(request):
    content = {
        'title'  : 'My First Post',
        'author' : 'Shibi',
        'body'   : 'Here is the body of my first blog',
        'now'    : datetime.datetime.now(),
    }
    
    return render_to_response('index.html', content)
"""

def home(request):
    entries = posts.objects.all()[:10]
    return render_to_response('index.html', { 'posts' : entries })


