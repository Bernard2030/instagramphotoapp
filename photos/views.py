from django.shortcuts import redirect, render,get_object_or_404
from django.http  import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from .forms import NewPostForm,SignUpForm,EditProfileForm,CommentForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import (DetailView)




# Create your views here.
# @login_required(login_url='/accounts/login/')
# def welcome(request):
#     return render(request, 'welcome.html')

@login_required(login_url = '/accounts/login/')
def index(request):
    posts = Post.all_images()
    return render(request, 'index.html',{'posts':posts})




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

            return redirect('timeline')

    else:
        form =NewPostForm()

    return render(request, 'new_post.html',{'form':form})  



@login_required(login_url='accounts/login')
def comment(request,id):

    id = id
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = request.user
            image = Post.objects.get(id = id)
            comment.pic_id = image
            comment.save()
            return redirect('timeline')


        else:
            pic_id = id
            messages.info(request,'make sure to fill all the fields as required')
            return redirect('comment',id=pic_id)

    else:
        id = id
        form = CommentForm
        return render(request, 'comment.html',{'form':form, 'id':id})


@login_required(login_url='accounts/login')
def single_pic(request,id):

    post = Post.objects.get(id = id)
    comments = Comments.objects.filter(pic_id = id)
    return render(request, 'single_pic.html',{'post':post,'comments':comments}) 



@login_required(login_url='accounts/login')
def logout_request(request):

    logout(request)
    return redirect('timeline')


class PostDetailview(DetailView):
    model = Post
    templete_name = 'single_pic.html'


    # def get_context_data(self, *args, **kwargs):
    #     context = super(PostDetailView, self).get_context_data(*args, **kwargs)
    #     stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()
    #     context ["total_likes"]=total_likes
    #     return context


    # def like_image(request, pk):
    #     post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #     post.likes.add(request.user)
    #     return HttpResponseRedirect(reverse('singlepic', args=[str(pk)]))



@login_required(login_url='accounts/login')
def add_like(request,post_id):
    post = Post.objects.filter(pk=post_id).first()
    post.likes += 1
    post.save()
    all_posts = Post.get_all_posts()
    context = {
        'pic': all_posts,
    }
    return render(request, 'index.html',context)



# @login_required(login_url='accounts/login')
# def search_results(request):
#     if 'image' in request.GET and request.GET['image']:
#         serch_term = request.GRT.get('image')
#         searched_pic = Post.search_image(search_term)
#         massage = f'{search_term}'

#         return render(request,'search.html', {'massage':massage,'image':searched_pics})

#     else:
#         message = "You have not entere anything to search" 
#         return render(request, 'search.html',{'message':message})   








    