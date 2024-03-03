from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Product, Group, ProductAccess, Lesson

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )

    def test_product_model(self):
        self.assertEqual(str(self.product), 'Test product')

class GroupModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )
        self.group = Group.objects.create(
            product=self.product,
            name='Test group'
        )

    def test_group_model(self):
        self.assertEqual(str(self.group), 'Test group')

class ProductAccessModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )
        self.group = Group.objects.create(
            product=self.product,
            name='Test group'
        )
        self.product_access = ProductAccess.objects.create(
            user=self.user,
            product=self.product,
            group=self.group
        )

    def test_product_access_model(self):
        self.assertEqual(str(self.product_access), 'testuser - Test product')

class LessonModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )
        self.lesson = Lesson.objects.create(
            product=self.product,
            name='Test lesson',
            video_link='https://example.com/video.mp4'
        )

    def test_lesson_model(self):
        self.assertEqual(str(self.lesson), 'Test lesson')

class ProductAPITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_products(self):
        Product.objects.create(
            creator=self.user,
            name='Test product 1',
            start_date=timezone.now(),
            price=100
        )
        Product.objects.create(
            creator=self.user,
            name='Test product 2',
            start_date=timezone.now(),
            price=200
        )
        response = self.client.get(reverse('product-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_product(self):
        product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )
        response = self.client.get(reverse('product-detail', args=[product.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test product')

class GroupAPITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )

    def test_list_groups(self):
        Group.objects.create(
            product=self.product,
            name='Test group 1'
        )
        Group.objects.create(
            product=self.product,
            name='Test group 2'
        )
        response = self.client.get(reverse('group-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_group(self):
        group = Group.objects.create(
            product=self.product,
            name='Test group'
        )
        response = self.client.get(reverse('group-detail', args=[group.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test group')

class ProductAccessAPITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )
        self.group = Group.objects.create(
            product=self.product,
            name='Test group'
        )

    def test_create_product_access(self):
        data = {
            'user': self.user.id,
            'product': self.product.id,
            'group': self.group.id
        }
        response = self.client.post(reverse('productaccess-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductAccess.objects.count(), 1)
        self.assertEqual(ProductAccess.objects.get().user, self.user)
        self.assertEqual(ProductAccess.objects.get().product, self.product)
        self.assertEqual(ProductAccess.objects.get().group, self.group)

    def test_list_product_accesses(self):
        ProductAccess.objects.create(
            user=self.user,
            product=self.product,
            group=self.group
        )
        ProductAccess.objects.create(
            user=self.user,
            product=self.product,
            group=self.group
        )
        response = self.client.get(reverse('productaccess-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_product_access(self):
        product_access = ProductAccess.objects.create(
            user=self.user,
            product=self.product,
            group=self.group
        )
        response = self.client.get(reverse('productaccess-detail', args=[product_access.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['product'], self.product.id)
        self.assertEqual(response.data['group'], self.group.id)

class LessonAPITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            creator=self.user,
            name='Test product',
            start_date=timezone.now(),
            price=100
        )

    def test_list_lessons(self):
        Lesson.objects.create(
            product=self.product,
            name='Test lesson 1',
            video_link='https://example.com/video1.mp4'
        )
        Lesson.objects.create(
            product=self.product,
            name='Test lesson 2',
            video_link='https://example.com/video2.mp4'
        )
        response = self.client.get(reverse('lesson-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_lesson(self):
        lesson = Lesson.objects.create(
            product=self.product,
            name='Test lesson',
            video_link='https://example.com/video.mp4'
        )
        response = self.client.get(reverse('lesson-detail', args=[lesson.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test lesson')
