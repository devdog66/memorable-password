import unittest
import sys
sys.path.append("../src")
from src.classes import RandomMethods

class Test_RandomMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.rm = RandomMethods()
        return super().setUp()

    def test_randomWord(self):
        wd = self.rm.randomWord(8, 32)
        print(wd)
        self.assertTrue(8 <= len(wd) <= 32)
    
    def test_randomSymbol(self):
        symb = self.rm.randomSymbol()
        print(symb)
        self.assertTrue(len(symb) == 1)

    def test_randomDigits(self):
        result = self.rm.randomDigits(6)
        print(result)
        self.assertTrue(len(result) == 6)

    def test_randomPassword(self):
        result = self.rm.randomPassword(16)
        print(result)

    def test_randomPasswords(self):
        self.rm.randomPasswords(20, 16)
        
        
if __name__ == '__main__':
    unittest.main()
