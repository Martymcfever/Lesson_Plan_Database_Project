from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from .forms import PostForm
from datetime import datetime
from .views import *
# Create your tests here.


class PostModelTestCase(TestCase):
    def setUp(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')

        self.post = Post.objects.create(title='Some title', pub_date=datetime.now(),
                                        contributors='Contributor(s) Name(s)', grade_level='GL', subject='Subject Name',
                                        description='This is a description', lesson_plan=dummy_file, verified=False)

    def test_model_fields_content(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')
        record = Post.objects.get(id=self.post.id)
        expected_field1 = record.title
        expected_field2 = datetime.now()
        expected_field3 = record.contributors
        expected_field4 = record.grade_level
        expected_field5 = record.subject
        expected_field6 = record.description
        expected_field8 = record.verified
        self.assertEqual(expected_field1, 'Some title')
        self.assertEqual(expected_field2, datetime.now())
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

