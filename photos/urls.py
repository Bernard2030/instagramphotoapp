from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.index,name = 'welcome'),
    url(r'^newpost/$',views.new_post,name='newpost'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
     url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^post/(\d+)',views.article,name ='post'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)