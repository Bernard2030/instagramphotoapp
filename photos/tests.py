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
