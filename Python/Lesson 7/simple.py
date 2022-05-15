################################################################################################################
####
#### Lesson 7: Simple Function
####
################################################################################################################

def sayHello():
    print("Hello from a function")

def getFullNamne(strFirstName, strLastName):
    strSurname = strFirstName + " " + strLastName
    return (strSurname)

def sayGreeting(strFullName):
    print("Hello " + strFullName + " nice to meet you!")

# Start with a simple welcome to tell the user what this program does
sayHello()

# Get the user's First Name
strFirstName = input ("PLease enter your first name")

# Get the user's Last Name
strLastName = input ("PLease enter your last name")

# Use the function to create their full name
strFullName = getFullNamne(strFirstName, strLastName)

# Use our function to Greet the user
sayGreeting(strFullName)

