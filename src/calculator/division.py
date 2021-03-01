class Calculator:
    def divide(self, a, b):

        result = a / b
        try:
            result = a/b
        except ZeroDivisionError:
            print('Division by 0 error')

        return result

