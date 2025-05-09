from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    pass
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users:user_profile', kwargs={'username': self.username})
    
    def get_n_posts(self):
        return self.post_set.count()
    def get_n_threads(self):
        return self.thread_set.count()