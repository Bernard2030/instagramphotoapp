from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url(r'^$',views.home,name='home'),
    url(r'^profile/(\d+)$',views.profile,name='profile'),
    url(r'^profile/update/(\d+)$',views.update_profile,name='update_profile'),
    url(r'no profile/(\d+)',views.nil_profile),
    url(r'^new/image/(\d+)$',views.new_image,name="new_image"),
    url(r'^comment/(\d+)$', views.comment, name='comment'),
    url(r'^comment/like/(\d+)$',views.like,name="like"),
    url(r'^image/update/(\d+)$',views.update_image,name='update_image'),
    url(r'^profile/follow/(\d+)$', views.follow, name='follow'),
    path('search_results/',views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)