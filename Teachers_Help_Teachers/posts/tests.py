from django.test import TestCase
from .models import Post
# Create your tests here.
class YourModelTest(TestCase):
    def setUp(self):
        YourModel.objects.create(field1='test 1', field2='test 2')

    def test_model_fields_content(self):
        record = YourModel.objects.get(id=1)
        expected_field1 = record.field1
        expected_field2 = record.field2
        self.assertEqual(expected_field1, 'test 1')
        self.assertEqual(expected_field2, 'test 2')
