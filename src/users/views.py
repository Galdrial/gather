from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from forum.models import Section, Thread, Post
from users.models import CustomUser
from django.views.generic import ListView





def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    user_threads = Thread.objects.filter(author=user).order_by('-pk')
    context = {
        'user': user,
        'user_threads': user_threads,
    }
    return render(request, 'users/user_profile.html', context)


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
   

    def get_queryset(self):
        return CustomUser.objects.all().order_by('username')