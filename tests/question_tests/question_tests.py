#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import check_if_prime, is_prime
from src.question_a.question_a import get_random_number

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())  # simple setup test

    def test_check_prime(self):
        from src.question_b.question_b import is_prime
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(11), True)

def test_config():
    return True
        
        
    def test_get_random_number(self):
        for _ in range(100):  # test multiple times to ensure randomness
            num = get_random_number()
            self.assertIn(num, range(1, 6))  # check if number is between 1 and 5

def test_config():
    return True
