from django.db import models
from django.conf import settings
from core.models import TimeStampModel
from core.admin import TimeStampModelAdmin
from django.urls import reverse
import math
from users.models import CustomUser


# Create your models here.


class Section(TimeStampModel):
    
    name = models.CharField(max_length=80)
    description = models.TextField()
    logo = models.ImageField()
  

    class Meta:
        verbose_name = 'Sezione'
        verbose_name_plural = 'Sezioni'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('forum:section_detail', kwargs={'pk': self.pk})
    
    def get_n_threads(self):
        return self.thread_set.count()
       

class Thread(TimeStampModel):
    title = models.CharField(max_length=120)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Discussione'
        verbose_name_plural = 'Discussioni'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:thread_detail', kwargs={'pk': self.pk})
    
    def get_n_pages(self):
        post_in_thread = self.post_set.count()
        n_pages = math.ceil(post_in_thread / 5)
        return n_pages
    
    def get_n_posts(self):
        return self.post_set.count()
  

class Post(TimeStampModel):
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)  # Utenti che hanno messo like

    class Meta:
        verbose_name = 'Messaggio'
        verbose_name_plural = 'Messaggi'

    def __str__(self):
        if len(self.content) > 10:
            return f"{self.content[:10]} ..."
        return self.author.username

