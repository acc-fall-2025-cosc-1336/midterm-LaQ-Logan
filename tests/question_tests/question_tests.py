#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import get_bonus_pay_amount, give_bonus_pay
from src.question_c.question_c import get_day_of_week, convert_day_number
from src.question_b.question_b import check_if_prime, is_prime
from src.question_a.question_a import get_random_number

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())  # simple setup test

    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1), (0.0, 0))
        self.assertEqual(get_bonus_pay_amount(200), (10.0, 0.05))
        self.assertEqual(get_bonus_pay_amount(600), (36.0, 0.06))
        self.assertEqual(get_bonus_pay_amount(1000), (70.0, 0.07))
        self.assertEqual(get_bonus_pay_amount(1500), (120.0, 0.08))
        self.assertEqual(get_bonus_pay_amount(2000), (0.0, 0))

def test_config():
    return True

    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid, please enter a number between 1 and 7.")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid, please enter a number between 1 and 7.")

def test_config():
    return True
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
