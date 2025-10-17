#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import get_bonus_pay_amount, give_bonus_pay

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1), (0.0, 0))
        self.assertEqual(get_bonus_pay_amount(200), (10.0, 0.05))
        self.assertEqual(get_bonus_pay_amount(600), (36.0, 0.06))
        self.assertEqual(get_bonus_pay_amount(1000), (70.0, 0.07))
        self.assertEqual(get_bonus_pay_amount(1500), (120.0, 0.08))
        self.assertEqual(get_bonus_pay_amount(2000), (0.0, 0))

def test_config():
    return True


