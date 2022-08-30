import unittest
from src.triangle import triangle

class TestTriangle(unittest.TestCase):
    
    def test_equilatero(self):
        self.assertEqual(triangle(5,5,5),'Equilátero')
    
    def test_escaleno(self):
        self.assertEqual(triangle(3,4,5),'Escaleno')
    
    def test_isosceles(self):
        self.assertEqual(triangle(5,5,9),'Isósceles')

    def test_zero(self):
        self.assertNotIn(triangle(0,5,9),['Isósceles','Equilátero','Escaleno'])
    
    def test_bigger(self):
        self.assertNotIn(triangle(8,8,16),['Isósceles','Equilátero','Escaleno'])
    
    def test_negative(self):
        self.assertNotIn(triangle(-3,4,5),['Isósceles','Equilátero','Escaleno'])

if __name__ == '__main__':
    unittest.main(verbosity=2)