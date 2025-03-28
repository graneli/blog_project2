from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'მომხმარებლის სახელი',
            'email': 'ელ.ფოსტა',
            'password': 'პაროლი'
        }

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'სათაური', 'class': 'form-control'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'დაწერე პოსტი', 'class': 'form-control', 'rows': 5})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'სათაური',
            'content': 'ტექსტი'
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'კომენტარი', 'class': 'form-control', 'rows': 3})
    )

    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'კომენტარი'
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        labels = {
            'bio': 'ბიოგრაფია',
            'profile_picture': 'პროფილის სურათი'
        }
