## @package docstring 
# tests-server.py 
# A file that has the tests that are related to server connectivity

from django.test import TestCase, Client
import requests

## This tests asserts if when the run server command is called that the webpage is actually up on the server and running.
class ServerRunningTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_server_running(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def check_server_running(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("The server is running.")
            else:
                print("The server is not running correctly.")
        except requests.exceptions.RequestException:
            print("The server is not running.")

    check_server_running("http://127.0.0.1:8000/")

