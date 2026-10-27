import csv
import os
from pathlib import Path
import tempfile
import unittest
from server import app

class PortfolioTests(unittest.TestCase):
    def test_pages_and_assets(self):
        client = app.test_client()
        for path in ('/', '/index.html', '/generic.html', '/elements.html', '/thankyou.html', '/static/assets/css/main.css', '/static/assets/js/main.js'):
            with self.subTest(path=path):
                with client.get(path) as response:
                    self.assertEqual(response.status_code, 200)

    def test_contact_submission(self):
        original = Path.cwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                response = app.test_client().post('/submit_form', data={'name': 'Test, Visitor', 'email': 'test@example.com', 'message': 'Hello'})
                self.assertEqual(response.status_code, 302)
                self.assertEqual(response.headers['Location'], '/thankyou.html')
                with open('database.csv', newline='') as saved:
                    self.assertEqual(list(csv.reader(saved)), [['Test, Visitor', 'test@example.com', 'Hello']])
            finally:
                os.chdir(original)
