################################################################################################################
####
#### Lesson 11: Process a long string in to 2 character outputs of 16 chars each
####
################################################################################################################
import time

# Start with a simple welcome
input_string = "hello this is an extremely long message indeed that will almost certainly exceed two lines of 16 characters"
print("Processing String: " + input_string)

offset = 0
str_len = len(input_string)

output_line1 = ""
output_line2 = ""

while offset < str_len:
    
    endl = offset + 16
    if (str_len < endl):
        endl = str_len

    output_line1 = input_string[offset:endl]

    endl = offset + 32
    if (str_len > endl):    
        if (str_len < endl):
            endl = str_len

        output_line2 = input_string[offset+16:endl]

    print(output_line1)
    print(output_line2, flush=True)

    offset +=1
    
    time.sleep(0.2)






