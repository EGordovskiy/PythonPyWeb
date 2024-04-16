from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.db_train_alternative.models import Author
from .serializers import AuthorModelSerializer


class AuthorViewSetTestCase(APITestCase):
    fixtures = ['testdata.json']
    def setUp(self):
        print('Создаем данные в БД')
        self.author1 = Author.objects.create(name='John', email='jhon@exampl.com')
        self.author2 = Author.objects.create(name='Alice', email='alice@cooper.com')

    def test_a_list_authors(self):
        print('Запуск теста test_list_authors')
        print('______________________________')
        print(f'В таблице "Автор" {Author.objects.count()} значений (-я)')
        # url = reverse('author-list')
        # url = 'http://127.0.0.1:8000/api/authors/'
        url = '/api/authors/'
        print(f'Проверяемый маршрут: {url}')
        response = self.client.get(url)
        print(f'Ответ от сервера: {response.status_code}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        print(f'Сериализатор вернул из БД: {serializer.data}')
        self.assertEqual(response.data, serializer.data)

    def test_b_create_author(self):
        print('Запуск теста test_create_author')
        print('_______________________________')
        # url = reverse('author-list')
        url = '/api/authors/'
        print(f'Проверяемый маршрут: {url}')
        data = {'name': 'Bob', 'email': 'bob@dilane.com'}
        response = self.client.post(url, data)
        print(f'Ответ от сервера: {response.status_code}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(name='Bob')
        serializer = AuthorModelSerializer(author)
        print(f'Сериализатор вернул из БД: {serializer.data}')
        self.assertEqual(response.data, serializer.data)

    def test_c_update_author(self):
        print("Запуск теста test_update_author")
        print("______________________________")
        # url = reverse('author-detail', kwargs={'pk': self.author1.pk})
        url = f'/api/authors/{self.author1.pk}/'
        print(f"Проверяемы маршрут: {url}")
        data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
        response = self.client.put(url, data)
        print(f"Ответ от сервера: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(pk=self.author1.pk)
        serializer = AuthorModelSerializer(author)
        print(f"Сериализатор вернул из БД: {serializer.data}")
        self.assertEqual(response.data, serializer.data)

    def test_d_partial_update_author(self):
        print("Запуск теста test_partial_update_author")
        print("______________________________")
        # url = reverse('author-detail', kwargs={'pk': self.author1.pk})
        url = f'/api/authors/{self.author1.pk}/'
        print(f"Проверяемы маршрут: {url}")
        data = {'name': 'John Doe'}
        response = self.client.patch(url, data)
        print(f"Ответ от сервера: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(pk=self.author1.pk)
        serializer = AuthorModelSerializer(author)
        print(f"Сериализатор вернул из БД: {serializer.data}")
        self.assertEqual(response.data, serializer.data)

    def test_e_delete_author(self):
        print("Запуск теста test_delete_author")
        print("______________________________")
        # url = reverse('author-detail', kwargs={'pk': self.author1.pk})
        url = url = f'/api/authors/{self.author1.pk}/'
        print(f"Проверяемы маршрут: {url}")
        response = self.client.delete(url)
        print(f"Ответ от сервера: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Author.objects.filter(pk=self.author1.pk).exists())
        print('Удалили автора')
