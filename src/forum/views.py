from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from forum.models import Section, Post, Thread
from forum.mixins import StaffRequiredMixin
from forum.forms import ThreadModelForm, PostModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from forum.models import Post
from django.http import JsonResponse


class AuthorDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("author-list")





class Homepage(ListView):
    queryset = Section.objects.all()
    template_name = 'forum/homepage.html'
    context_object_name = 'sections'

class SectionCreateView(StaffRequiredMixin, CreateView):
    model = Section
    fields = ['name', 'description', 'logo']
    template_name = 'forum/section_create.html'
    success_url = '/'

def section_detail_view(request, pk):
    section_obj = get_object_or_404(Section, pk=pk)
    section_threads = Thread.objects.filter(section=section_obj).order_by('-created')
    context = {
        'section': section_obj,
        'section_threads': section_threads,
    }
    return render(request, 'forum/section_detail.html', context)

@login_required
def thread_create_view(request, pk):
    section_obj = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = ThreadModelForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.section = section_obj
            thread.author = request.user
            thread.save()
            first_post = Post.objects.create(
                thread=thread,
                author=request.user,
                content=form.cleaned_data['first_post_content'],
            )
            return HttpResponseRedirect(section_obj.get_absolute_url())
    else:
        form = ThreadModelForm()
    context = {
        'form': form,
        'section': section_obj,
    }
    return render(request, 'forum/thread_create.html', context)

def thread_detail_view(request, pk):
    thread_obj = get_object_or_404(Thread, pk=pk)
    thread_posts = Post.objects.filter(thread=thread_obj).order_by('id')
    paginator = Paginator(thread_posts, 10)  # Show 10 posts per page
    page = request.GET.get('pagina')
    current_page_posts = paginator.get_page(page)

    post_create_form = PostModelForm()

    context = {
        'thread': thread_obj,
        'thread_posts': current_page_posts,
        'post_create_form': post_create_form,
    }
    return render(request, 'forum/thread_detail.html', context)

@login_required
def post_create_view(request, pk):
    thread_obj = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread_obj
            post.author = request.user
            post.save()
            thread_url = thread_obj.get_absolute_url()
            thread_pages = thread_obj.get_n_pages()
            if thread_pages > 1:
                success_url = f"{thread_url}?pagina={thread_pages}"
                return HttpResponseRedirect(success_url)
            else:
                return HttpResponseRedirect(thread_url)

            
    else:
        return HttpResponseBadRequest()

    return HttpResponseRedirect(thread_obj.get_absolute_url())


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'forum/post_confirm_delete.html'
   

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    def get_success_url(self):
        thread = self.get_object().thread
        return thread.get_absolute_url()
       

@login_required
def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if post.liked_by.filter(id=user.id).exists():
            post.liked_by.remove(user)
            post.like -= 1
            liked = False
        else:
            post.liked_by.add(user)
            post.like += 1
            liked = True

        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseBadRequest()




