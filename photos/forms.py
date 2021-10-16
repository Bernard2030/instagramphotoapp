from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile,Post,Comments

class signUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Input a valid email.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email =forms.EmailField(max_length=200, help_text='. Input valid email address.')  

    class Meta:
        model = User
        fields = ('usename', 'email') 

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile+image', 'bio']

class PostForm(forms.modelform):
    class Meta:
        model = Post
        friends = ('image', 'caption')

class CommentsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add your comment ...'

        class Meta:
            model = Comments
            fields = ('comments')                
