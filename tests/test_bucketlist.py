import module_import
from app.model import Users
import unittest

class BaseTest(unittest.TestCase):
    ## Login set up now.
    def setUp(self):
        self.users = Users()

    ## Test empty fields.
    def test_adding_bucket(self):
        ##app_login = App()
        result = self.users.add_bucket('', '')
        ##self.assertEqual(True, result, 'Username and password cannot be empty')
        self.assertTrue(result, "Bucket Name cannot be empty")

    
if __name__ == '__main__':
    unittest.main()