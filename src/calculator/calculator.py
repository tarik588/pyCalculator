import math
class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self,a,b):
        result = a+b
        return result

    def divide(self,a,b):
        result = a/b
        return result


    def multiply(self, a, b):
        result = a * b
        return result

    def subtraction(self,a,b):
        result = a-b
        return result

    def sqrt(self,a,b):
        result = math.sqrt(a,b)
        return result

