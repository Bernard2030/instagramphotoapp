from django.shortcuts import redirect, render,get_object_or_404
from django.http  import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from .forms import NewPostForm,SignUpForm,EditProfileForm,CommentForm




# Create your views here.
# @login_required(login_url='/accounts/login/')
# def welcome(request):
#     return render(request, 'welcome.html')

@login_required(login_url = '/accounts/login/')
def index(request):
    posts = Post.all_images()
    return render(request, 'index.html',{'posts':posts})


# def signUp(request):    
#     if request.method=='POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             name=form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             # send=welcome_email(name,email)
#             HttpResponseRedirect('timeline')

#     else:
#         form = SignUpForm()

#     return render(request,'registration/registration_form.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):

    user_posts = Post.user_pics(request.user)
    return render(request, 'profile.html',{'user_posts':user_posts})  

@login_required(login_url='accounts/login')
def edit_profile(request):

    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'update_profile.html',{'form':form})

@login_required(login_url='accounts/login')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('welcome')

    else:
        form =NewPostForm()

    return render(request, 'new_post.html',{'form':form})                


    