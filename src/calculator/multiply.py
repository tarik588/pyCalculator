class Calculator:
    def multiply(self, a, b):
        result = a * b
        return result

Calculator.multiply = staticmethod(Calculator.multiply)