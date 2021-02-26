import fibonacci
import unittest

class fibTesting(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci.fib(4), 3)
    
if __name__ == "__main__":
    unittest.main()