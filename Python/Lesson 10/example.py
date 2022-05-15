################################################################################################################
####
#### Lesson 10: Importing Modules
####
################################################################################################################
import CodeCamp.Modules

# Start with a simple welcome to tell the user what this program does
print("Code Camp Calculator")

# Program continuaton Flag
bContinue = True
while bContinue == True:

    # Ask for the first number
    strInput = input ("Please enter your first number")
    nNumber1 = 0
    if strInput.isnumeric():
        nNumber1 = int(strInput)
    else:
        print ("your first number must be a numeric value")

    # Ask for the second number
    strInput = input ("Please enter your second number")
    nNumber2 = 0
    if strInput.isnumeric():
        nNumber2 = int(strInput)
    else:
        print ("your second number must be a numeric value")

    # Ask what type of operation we're going to do
    strInput = input ("What Sum would you like to do? \nOptions: + - x /")
    
    # Work out the result
    calc = CodeCamp.Modules.Calculator(nNumber1, nNumber2)

    if strInput == "+":
        nResult = calc.Add()
        
    elif strInput == "-":
        nResult = calc.Subtract()

    elif strInput == "/":
        nResult = calc.Divide()

    elif strInput == "x":
        nResult = calc.Multiply()

    # Output a response using the user's name
    print ("Answer: " + str(nResult))

    # Ask if the user wants to continue
    strInput = input ("Would you like to perform another calcalation?: Y/n?")

    # Convert the response to our Continue flag
    bContinue = (strInput == "Y")

    if bContinue == False:
        for strCalc in calc.Calculations:
            print (strCalc)

