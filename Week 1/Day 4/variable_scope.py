message = "Global Message"

def show_message():
    message = "Local Message"
    print("Inside function:", message)

show_message()  
# Output: Inside function: Local Message
print("Outside function:", message)  
# Output: Outside function: Global Message
