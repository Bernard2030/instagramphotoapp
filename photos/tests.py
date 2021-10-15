from django.test import TestCase
from .models import Post,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
#set up method
    def setUp(self):
        self.bernard = Profile(name = "bernard")

#Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bernard, Profile))    

    #Testing save method
    def test_save_method(self):
        self.bernard.save_profile()
        profiles = Profile.objects.all()
        self.asserttrue(len(profiles) > 0)

class PostTestClass(TestCase): 
    def setUp(self):
        #creating a new post and saving it
        self.bernard = Post(name = "bernard")
        self.bernard.save_post()

        #creating a new image and saving it
        self.new_Post = Post(name = 'squid')   
        self.new_Post.save() 

    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()
            
