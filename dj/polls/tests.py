from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from polls.models import BlogPost


class PostApiTests(APITestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(title='Старий', content='Текст')
        self.list_url = '/api/posts/'
        self.detail_url = f'/api/posts/{self.post.pk}/'

    def test_list_returns_200(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_returns_201(self):
        data = {'title': 'Новий', 'content': 'Текст'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)

    def test_create_without_title_returns_400(self):
        response = self.client.post(self.list_url, {'content': 'Текст'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_missing_post_returns_404(self):
        response = self.client.get('/api/posts/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_without_content_returns_400(self):
        response = self.client.put(self.detail_url, {'title': 'Новий'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_changes_only_sent_fields(self):
        response = self.client.patch(self.detail_url, {'title': 'Новий'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Новий')
        self.assertEqual(self.post.content, 'Текст')

    def test_delete_returns_204_then_404(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
