################################################################################################################
####
#### Lesson 3: 
####
################################################################################################################

# Start with a simple welcome to tell the user what this program does
print("Add two numbers...")

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
strResult = nNumber1 + nNumber2

# Output a response using the user's name
print ("Answer: " + str(strResult))


