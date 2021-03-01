class Calculator:

    def subtraction(self, a, b):
        result = a - b
        return result

Calculator.subtraction = staticmethod(Calculator.subtraction)