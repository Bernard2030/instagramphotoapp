from django import forms
from .models import Post,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter Email!')

    class Meta:
        model = User
        fields = ('username','email','password1','password2') 


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image','bio','username')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','pic_id']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','likes']

     
