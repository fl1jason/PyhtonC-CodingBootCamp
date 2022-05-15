################################################################################################################
####
#### Lesson 8: Simple Classes
####
################################################################################################################

class Calculator:
    Number1 = 0
    Number2 = 0

    def __init__(self, number1, number2):
        self.Number1 = number1
        self.Number2 = number2

    def Add(self):
        nResult = self.Number1 + self.Number2
        return (nResult)

calc = Calculator(1, 87)
result = calc.Add()

print (str(result))

