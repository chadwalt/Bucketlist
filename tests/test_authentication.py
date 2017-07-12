import module_import
from app.application import App
import unittest

class test_authentication(unittest.TestCase):
    ## Login set up now.
    def setUp(self):
        self.app_login = App()

    ## Test empty fields.
    def test_empty_fields(self):
        ##app_login = App()
        result = self.app_login.login('', '')
        ##self.assertEqual(True, result, 'Username and password cannot be empty')
        self.assertTrue(result, "Username and Password cannot be empty")

    def test_login_match(self):
        result = self.app_login.login('chad', 'chad123')
        self.assertTrue(result, "Passwords didn't match")
        

if __name__ == '__main__':
    unittest.main()