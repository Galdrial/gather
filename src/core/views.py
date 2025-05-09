from django.shortcuts import render
from core.utils import perform_search
from forum.models import Post  # Import the Post model

def search_view(request):
    querystring = request.GET.get('q', '')
    threads, posts, users = perform_search(querystring)
    
    context = {
        'querystring': querystring,
        'threads': threads,
        'posts': posts,
        'users': users,
    }
    
    return render(request, 'core/search.html', context)





    