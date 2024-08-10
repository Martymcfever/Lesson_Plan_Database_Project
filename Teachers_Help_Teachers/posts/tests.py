from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from .forms import PostForm
from datetime import timezone
from .views import *
from .models import Post
import os
from posts.views import download_file
# Create your tests here.


class PostModelTestCase(TestCase):
    def setUp(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')

        self.post = Post.objects.create(title='Some title', pub_date=timezone.now(),
                                        contributors='Contributor(s) Name(s)', grade_level='GL', subject='Subject Name',
                                        description='This is a description', lesson_plan=dummy_file, verified=False)

    def test_model_fields_content(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')
        record = Post.objects.get(id=self.post.id)

        expected_field1 = record.title
        expected_field2 = timezone.now()
        expected_field3 = record.contributors
        expected_field4 = record.grade_level
        expected_field5 = record.subject
        expected_field6 = record.description
        expected_field8 = record.verified

        time_diff = abs((expected_field2 - timezone.now()).total_seconds())

        self.assertEqual(expected_field1, 'Some title')
        self.assertAlmostEqual(time_diff, 0, delta=1)
        self.assertEqual(expected_field3, 'Contributor(s) Name(s)')
        self.assertEqual(expected_field4, 'GL')
        self.assertEqual(expected_field5, 'Subject Name')
        self.assertEqual(expected_field6, 'This is a description')
        self.assertEqual(self.post.lesson_plan.read(), dummy_file.read())
        self.assertEqual(expected_field8, False)

    def tearDown(self):
        self.post.delete()


class AddFunctionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_url = reverse('add')

    def test_add_function_POST(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')
        dummy_lesson_file = SimpleUploadedFile("lesson.txt", b"lesson content")

        response = self.client.post(self.add_url, {
            'title': 'test_title',
            'file_field': dummy_file,
            'contributors': 'test contributor',
            'grade_level': '12',
            'subject': 'test subject',
            'description': 'test description',
            'lesson_plan': dummy_lesson_file,
        })

        self.assertEqual(response.status_code, 302)  # check for redirect status code
        self.assertRedirects(response, self.add_url)  # check if it redirects to add_function

        # Now send a GET request to check if the form is instance of PostForm
        response = self.client.get(self.add_url)
        self.assertIsInstance(response.context['form'], PostForm)

class SearchFunctionViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search')  # use the actual name of search_function url
        self.test_post = Post.objects.create(title='test_title')  # create a post to search for

    def test_search_function_POST(self):
        response = self.client.post(self.search_url, {'searched': 'test_title'})


        # Check the response status
        self.assertEqual(response.status_code, 200)

        # Check that the response context contains the 'searched' query and 'results'
        self.assertEqual(response.context['searched'], 'test_title')
        self.assertIn(self.test_post, response.context['results'])

    def test_search_function_no_POST_data(self):
        response = self.client.get(self.search_url)

        # Check the response status
        self.assertEqual(response.status_code, 200)


class DownloadFileViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        dummy_lesson_file = SimpleUploadedFile("lesson.txt", b"lesson content")  # creates a file for testing
        self.test_post = Post.objects.create(
            title='test_title',
            lesson_plan=dummy_lesson_file,
            pub_date=timezone.now(),
            contributors='Contributor(s) Name(s)',
            grade_level='GL',
            subject='Subject Name',
            description='This is a description',
            verified=False,
        )

    def test_download_file(self):
        download_url = reverse('download', args=[
            self.test_post.id])
        response = self.client.get(download_url)

        # Check the response status
        self.assertEqual(response.status_code, 200)

        # Check the content of the response. It should match the content of the test file
        response_content = b"".join(response.streaming_content)
        self.assertEqual(response_content, b"lesson content")

    def tearDown(self):
        # Delete the test file from the file system
        if os.path.isfile(self.test_post.lesson_plan.path):
            os.remove(self.test_post.lesson_plan.path)

        # Delete the test post object
        self.test_post.delete()

        super().tearDown()
