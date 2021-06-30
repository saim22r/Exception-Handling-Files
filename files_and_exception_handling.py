# print(1/0) # ZeroDivisionError: division by zero

# num = 9
# if num > 8 # No colon = SyntaxError: invalid syntax
#     print(num)

# We will create a file with required permission and see what errors/exception are possible to be seen
# First iteration
# file = open("order.text") # open() takes a string arg with file name
# print(file) # Let's see the outcome and record it. File not found error will appear.

# Second iteration
try:
    file = open("order.text")
    print("File found") # Try block required except or will throw an error
except FileNotFoundError as errmsg: # Creating alias same as a nickname
    print(f"File not found {errmsg}")
finally: # Finally will execute regardless of try and except block execution, also used to clean up the code
    print("Thank you for visiting, see you again!")

# Let's create a file now called order.text and run the code

# Let's apply DRY - OOP - Python Packaging
             # 1     2           3

# create function
# create a class
# create a package