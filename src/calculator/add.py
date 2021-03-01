class Calculator:
    def add(self, a, b):
        result = a + b
        return result
Calculator.add = staticmethod(Calculator.add)