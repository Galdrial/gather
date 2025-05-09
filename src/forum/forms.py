from django import forms
from forum.models import Thread, Post


class ThreadModelForm(forms.ModelForm):
    first_post_content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Di cosa vuoi parlarci?'}),
        max_length=4000,
        label='Primo Messaggio del Thread',
    )
    

    class Meta:
        model = Thread
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titolo della discussione'}),
        }

class PostModelForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'content': 'Messaggio',
        }