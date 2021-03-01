import math
class Calculator:
    def sqrt(self, a):
        result = math.sqrt(a)
        return result

Calculator.sqrt = staticmethod(Calculator.sqrt)