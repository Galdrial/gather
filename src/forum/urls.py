from django.urls import path
from forum import views
from .views import like_post


app_name = 'forum'

urlpatterns = [
    path('', views.Homepage.as_view(), name='forum_homepage'),   
    path('section-create/', views.SectionCreateView.as_view(), name='section_create'),
    path('section/<int:pk>/thread-create/', views.thread_create_view, name='thread_create'),
    path('section-detail/<int:pk>/', views.section_detail_view, name='section_detail'),
    path('section/<int:pk>/thread-detail/', views.thread_detail_view, name='thread_detail'),
    path('thread/<int:pk>/create-post/', views.post_create_view, name='post_create'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/like/', like_post, name='like_post'),
   
]