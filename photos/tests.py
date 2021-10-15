from django.test import TestCase
from .models import Post,Profile

# Create your tests here.

#set up method
def setUp(self):
    self.bernard = Profile(name = "bernard", user = "moringa")

#Testing Instance
def test_instance(self):
    self.assertTrue(isinstance(self.bernard, Profile))    