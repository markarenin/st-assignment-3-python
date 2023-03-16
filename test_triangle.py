import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
  
  def test_equilateral_triangle(self):
    self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
    self.assertEqual(classify_triangle(200, 200, 200), "Equilateral")
  
  def test_isosceles_triangle(self):
    # One pair of sides is equal
    self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
    self.assertEqual(classify_triangle(199, 199, 198), "Isosceles")
  
  def test_scalene_triangle(self):
    self.assertEqual(classify_triangle(2, 3, 4), "Scalene")
    self.assertEqual(classify_triangle(97, 98, 99), "Scalene")
    
  def test_not_a_triangle(self):
    self.assertEqual(classify_triangle(1, 1, 2), "NotATriangle")
    self.assertEqual(classify_triangle(100, 100, 200), "NotATriangle")

  def test_invalid_values(self):
    self.assertEqual(classify_triangle(0,0,0), "Invalid values.")
    self.assertEqual(classify_triangle(201,201,201), "Invalid values.")
    