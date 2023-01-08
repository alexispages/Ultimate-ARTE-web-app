import unittest
from app import app
from bs4 import BeautifulSoup

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.testing = True

    def test_status_code_index(self):
        result = self.app.get('http://127.0.0.1:5000/arte')
        self.assertEqual(result.status_code, 200)

    def test_status_code_programmedujour(self):
        result = self.app.get('http://127.0.0.1:5000/arte/programme_du_jour')
        self.assertEqual(result.status_code, 200)

    def test_status_code_categories(self):
        result = self.app.get('http://127.0.0.1:5000/arte/categories')
        self.assertEqual(result.status_code, 200)

    def test_table_exists(self):
        response = self.app.get('http://127.0.0.1:5000/arte/programme_du_jour')
        soup = BeautifulSoup(response.data, 'html.parser')
        table = soup.find('table')
        self.assertIsNotNone(table)   

if __name__ == '__main__':
    unittest.main()