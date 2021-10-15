from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    profile_image =models.ImageField(upload_to='profile_image/', default='default.png')  
    bio = models.TextField(max_length=500, default='My Bio', blank=True) 
    name = models.CharField(blank=True, max_length=120)
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    
    def __str__(self):
        return f'{self.user.username} Profile'


    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()                  

          


class Post(models.Model):
    images = models.ImageField(upload_to='images/')
    name =models.CharField(max_length=60, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    comments = models.CharField(max_length=200)

    class Meta:
        ordering = ["-pk"]

    @property
    def get_all_comments(self):
        return self.comments.all()
    def save_images(self):
        self.save()

    def delete_images(self):
        self.delete()

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return f'{self.user.name}Post'                    


 

# class Comment(models.Model):
#     comment = models.TextField()
#     images = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments') 

#     def __str__(self):
#         return f'{self.user.name} Comment'

#     class Meta:
#         ordering = ["-pk"]     

