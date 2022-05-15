################################################################################################################
####
#### Lesson 8: Simple Classes
####
################################################################################################################

class Calculator:
    Number1 = 0
    Number2 = 0
    Calculations = [""]

    def __init__(self, number1, number2):
        self.Number1 = number1
        self.Number2 = number2
        self.Calculations.clear()

    def Add(self):
        nResult = self.Number1 + self.Number2; 

        self.Calculations.append(str(self.Number1) + " + " + str(self.Number2) + " = " + str(nResult))

        return (nResult)

    def Subtract(self):
        nResult = self.Number1 - self.Number2; 

        self.Calculations.append(str(self.Number1) + " - " + str(self.Number2) + " = " + str(nResult))
        return (nResult)

    def Multiply(self):
        nResult = self.Number1 * self.Number2; 

        self.Calculations.append(str(self.Number1) + " X " + str(self.Number2) + " = " + str(nResult))
        return (nResult)
    
    def Divide(self):
        nResult = self.Number1 / self.Number2; 

        self.Calculations.append(str(self.Number1) + " / " + str(self.Number2) + " = " + str(nResult))
        return (nResult)
