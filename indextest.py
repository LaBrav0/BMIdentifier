import unittest
from app import weight_bmi

class TestBMIWeightCategorization(unittest.TestCase): #The following test cases below use the 'self.assertEqual' function to check if a value returns true within certain parameters.
    def test_underweight(self):
        # Test Case for BMI values below 18.5
        for bmi in [10, 15, 18.4]:
            self.assertEqual(weight_bmi(bmi), 'Underweight')

    def test_normalweight(self):
        # Test Case for BMI values between 18.5 and 24.9
        for bmi in [19, 22, 24.8]:
            self.assertEqual(weight_bmi(bmi), 'Normal weight')

    def test_overweight(self):
        # Test Case for BMI values between 25 and 29.9
        for bmi in [25, 27, 29.8]:
            self.assertEqual(weight_bmi(bmi), 'Overweight')

    def test_obese(self):
        # Test Case for BMI values 30 and above
        for bmi in [30, 37, 90]:
            self.assertEqual(weight_bmi(bmi), 'Obese')

if __name__ == '__main__':
    unittest.main()
