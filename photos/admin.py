from django.contrib import admin
from .models import Comments, Follow, Profile,Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Follow)

