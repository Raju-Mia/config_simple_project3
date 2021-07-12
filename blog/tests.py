from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='rajucse00@email.com',
            password='12345678'
        )
        self.post = Post.objects.create(
            tital='A good tital',
            body='Nice body content',
            author=self.user,
        )
    def test_string_representation(self):
        post = Post(tital='A sample tital')
        self.assertEqual(str(post), post.tital)
    
    def test_get_absolute_url(self): # new
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')


    def test_post_content(self):
        self.assertEqual(f'{self.post.tital}', 'A good tital')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good tital')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self): # new
        response = self.client.post(reverse('post_new'), {
            'tital': 'New tital',
            'body': 'New text',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().tital, 'New tital')
        self.assertEqual(Post.objects.last().body, 'New text')


    def test_post_update_view(self): # new
        response = self.client.post(reverse('post_edit', args='1'), {
            'tital': 'Updated tital',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)


    def test_post_delete_view(self): # new
        response = self.client.post(
            reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
