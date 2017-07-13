import module_import
from app.model import Bucket
import unittest

class BaseTest(unittest.TestCase):
    ## Login set up now.
    def setUp(self):
        self.bucket = Bucket()

    ## Test empty fields.
    def test_adding_bucket_item(self):
        result = self.bucket.add_item('', '')
        ##self.assertEqual(True, result, 'Username and password cannot be empty')
        self.assertFalse(result, "Bucket Name cannot be empty")

    ## Test empty fields.
    def test_edit_bucket_item(self):
        result = self.bucket.edit_item('', '')
        self.assertFalse(result, "ID and name cannot be empty")        

    
if __name__ == '__main__':
    unittest.main()