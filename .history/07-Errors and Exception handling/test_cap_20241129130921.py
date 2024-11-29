'''
A simple testing logic python script using unittest
'''
import unittest
import cap 

# we will inherit TestCase class  that comes with unittest 
def test_text_input(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")

    def test_mulitple_words(self):
        text = "hello world"
        result = cap.cap_text(self)
        self.assertEqual(result, "Hello World")