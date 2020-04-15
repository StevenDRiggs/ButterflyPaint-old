import unittest

from random import randint

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


    def status_code_check(self, address, code=200, **kwargs):
        result = self.app.get(address, **kwargs)
        self.assertEqual(result.status_code, code)


    def test_splash_status_code(self):
        self.status_code_check('/')

    def test_index_status_code(self):
        self.status_code_check('/index')

    def test_database_status_code(self):
        self.status_code_check('/database')

    def test_database_add_status_code(self):
        self.status_code_check('/database/add')

    def test_database_add_single_status_code(self):
        self.status_code_check('/database/add/single')

    def test_database_add_batch_status_code(self):
        self.status_code_check('/database/add/batch')

    def test_database_update_status_code(self):
        self.status_code_check('/database/update')

    def test_database_update_single_status_code(self):
        self.status_code_check('/database/update/single')

    def test_database_update_single_color_idstatus_code(self):
        color_id = randint(1, 5)
        self.status_code_check(f'/database/update/single/{color_id}')

    def test_database_update_batch_status_code(self):
        self.status_code_check('/database/update/batch')

    def test_database_update_batch_update_status_code(self):
        self.status_code_check('/database/update/batch/update', choices=[('a', 1), ('b', 2), ('c', 3)])


if __name__ == '__main__':
    unittest.main()
