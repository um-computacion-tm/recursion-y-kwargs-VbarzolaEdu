import unittest
def factorial(n):
    if n== 0 or n == 1:
        return 1
    else:
        if n >= 2:
            return n * factorial(n-1)
            
class testfactorial(unittest.TestCase):
    def test_0(self):
        resultado=factorial(0)
        self.assertEqual(resultado,1)
    def test_1(self):
        resultado=factorial(1)
        self.assertEqual(resultado,1)
    def test_2(self):
        resultado=factorial(2)
        self.assertEqual(resultado,2)
    def test_3(self):
            resultado=factorial(3)
            self.assertEqual(resultado,6)
    def test_4(self):
        resultado=factorial(4)
        self.assertEqual(resultado,24)
    def test_5(self):
        resultado=factorial(5)
        self.assertEqual(resultado,120)
    def test_6(self):
        resultado=factorial(6)
        self.assertEqual(resultado,720)
    def test_7(self):
        resultado=factorial(7)
        self.assertEqual(resultado,5040)
unittest.main()