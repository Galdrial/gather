from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('user-profile/<str:username>/', views.user_profile_view, name='user_profile'),
    path('user-list/', views.UserListView.as_view(), name='user_list'),
]