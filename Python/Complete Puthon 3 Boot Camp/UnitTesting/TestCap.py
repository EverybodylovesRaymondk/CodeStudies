Importing the unittest package
import unittest
#Importing the module to test 
import Cap

class TestCap(unittest.TestCase):
    def test_one_word(self)    :
        text='python'
        result = Cap.Cap_text(text)
        self.assertEquals( result,'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result2 = Cap.Cap_text(text)
        self.assertEqual(result2,'Monty Python')
        
if __name__ == '_-main__':
    unittest.main()