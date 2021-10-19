from django.test import TestCase

from .models import Image,Comment

# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.bernard= Image(first_name = 'bernard', last_name ='Opiyo', email ='brobernar.254@gmail.com.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.bernard,Image))

    def test_save_method(self):
        self.bernard.save_post()
        editors = Image.objects.all()
        self.assertTrue(len(editors) > 0)


class CommentTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.bernard= Image(first_name = 'Bernard', last_name ='Opiyo', email ='brobernard.254@gmail.com')
        self.bernard.save_post()

        # Creating a new tag and saving it
        self.new_tag = Comment(name = 'testing')
        self.new_tag.save()

        self.new_article= Comment(title = 'Test Article',post = 'This is a random test Post',editor = self.bernard)
        self.new_article.save()

        self.new_article.author.add(self.new_tag)

    def tearDown(self):
        Comment.objects.all().delete()
        Comment.objects.all().delete()
        Comment.objects.all().delete()