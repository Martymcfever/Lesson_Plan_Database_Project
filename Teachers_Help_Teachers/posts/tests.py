from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Post
import datetime
# Create your tests here.


class PostModelTestCase(TestCase):
    def setUp(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')

        self.post = Post.objects.create(title='Some title', pub_date=datetime.datetime.now(),
                                        contributors='Contributor(s) Name(s)', grade_level='GL', subject='Subject Name',
                                        description='This is a description', lesson_plan=dummy_file, verified=False)

    def test_model_fields_content(self):
        dummy_file = SimpleUploadedFile('test.txt', b'Test content')
        record = Post.objects.get(id=self.post.id)
        expected_field1 = record.title
        expected_field2 = datetime.datetime.now()
        expected_field3 = record.contributors
        expected_field4 = record.grade_level
        expected_field5 = record.subject
        expected_field6 = record.description
        expected_field8 = record.verified
        self.assertEqual(expected_field1, 'Some title')
        self.assertEqual(expected_field2, datetime.datetime.now())
        self.assertEqual(expected_field3, 'Contributor(s) Name(s)')
        self.assertEqual(expected_field4, 'GL')
        self.assertEqual(expected_field5, 'Subject Name')
        self.assertEqual(expected_field6, 'This is a description')
        self.assertEqual(self.post.lesson_plan.read(), dummy_file.read())
        self.assertEqual(expected_field8, False)

    def tearDown(self):
        self.post.delete()
