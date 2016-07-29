from unittest import TestCase
from primes import is_prime

class TestIs_prime(TestCase):

    def test_is_prime(self):
        #self.fail()
        #self.assertTrue(1 == 1)
        self.assertTrue(is_prime(5))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(6))
