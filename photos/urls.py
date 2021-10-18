from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.index,name = 'timeline'),
    url(r'^newpost/$',views.new_post,name='newpost'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url('comment/<int:id>/',views.comment,name='comment'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url('post/<int:post_id>/like', views.add_like, name='time'),
    #url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^singlepic/(\d+)',views.single_pic,name='singlepic'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^post/(\d+)',views.article,name ='post'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)