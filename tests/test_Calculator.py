import unittest
from src.calculator.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)
   
    def addtest(self):
        tester = csvRead(..tests/Unit Test Additon.csv)
        for row in test:
            result = int(row['results']
            self.assertEqual(self.calculator.add(row['value 1', row['value 2], result)
                                    
      def subtracttest(self):
        tester = csvRead(..tests/Unit Test Subtration.csv)
        for row in test:
            result = int(row['results']
            self.assertEqual(self.calculator.add(row['value 1', row['value 2], result)
             
        def multitest(self):
        tester = csvRead(..tests/Unit Test Multiplication.csv)

                                                                   

print()


