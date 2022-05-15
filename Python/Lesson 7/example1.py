################################################################################################################
####
#### Lesson 7: Functions
####
################################################################################################################

# Start with a simple welcome to tell the user what this program does
print("Add two numbers...")

def calculateAdd(nFirstNumber, nSecondNumber):
    
    nResult = nFirstNumber + nSecondNumber
    return (nResult)

# Counter so we know how many calculations are being done
nNumberOfCalculations = 0

# String Array so we can keep a track of each culculation
strCalculations = [""]
strCalculations.clear()

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

    # Work out the result
    nResult = calculateAdd(nNumber1, nNumber2)

    # Output a response using the user's name
    print ("Answer: " + str(nResult))

    # Add our sum in to the Array
    strCalculations.append (str(nNumber1) + " + " + str(nNumber2) + " = " + str(nResult))

    # Ask if the user wants to continue
    strInput = input ("Would you like to add 2 more numbers: Y/n?")

    # Convert the response to our Continue flag
    bContinue = (strInput == "Y")
    
    if bContinue == True:
        nNumberOfCalculations = nNumberOfCalculations + 1
    else:
        nNumberOfCalculations = len(strCalculations)
        print ("You have made " + str(nNumberOfCalculations) + " calculations")

        # Use a standard For loop to iterate through an array
        for strCalculation in strCalculations:
            print (strCalculation)

        print ("... or in reverse order ...")

        # Use a standard For loop to iterate through an array
        for nItem in range(nNumberOfCalculations, 0, -1):
            print (strCalculations[nItem - 1])


