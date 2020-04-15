import unittest

from bpaint import app


class TestValidURLs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass


    def test_splash_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_index_status_code(self):
        result = self.app.get('/index')
        self.assertEqual(result.status_code, 200)

    def test_database_status_code(self):
        result = self.app.get('/database')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
