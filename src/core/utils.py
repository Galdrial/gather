from forum.models import Thread, Post
from users.models import CustomUser

def perform_search(querystring):
    if querystring == "" or querystring.isspace():
        return [], [], []
    threads = Thread.objects.filter(title__icontains=querystring)
    posts = Post.objects.filter(content__icontains=querystring)
    users = CustomUser.objects.filter(username__icontains=querystring)
    return threads, posts, users

