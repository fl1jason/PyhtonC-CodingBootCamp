################################################################################################################
####
#### Lesson 4: While Loops and Evaluation
####
################################################################################################################

# Start with a simple welcome to tell the user what this program does
print("Add two numbers...")

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

    # Wo
    #rk out the result
    strResult = nNumber1 + nNumber2

    # Output a response using the user's name
    print ("Answer: " + str(strResult))

    # Ask if the user wants to continue
    strInput = input ("Would you like to add 2 more numbers: Y/n?")

    # Convert the response to our Continue flag
    bContinue = (strInput == "Y")

