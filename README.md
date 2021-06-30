# Working wih Files
## Exception handling
### File Permissions

#### Examples of errors
- `value error`
- `syntax error`
- `out of bounce`
- `key error`
- `attribute error`
- `ZeroDivisionError: division by zero`

#### File Permissions
- `r` This is the default mode. It opens a file for reading
- `w` This mode opens file for writing. If the file doesn't exist,  it creates a new file.
- `x` Creates a new file, if already exists, the operation fails
- `a` Open file in Append Mode, if file doesn't exist it creates a new one
- `t` This is the default mode to open in text mode
- `b` This is for binary mode
- `+` This will open a file for reading and writing (updating)

**We have `try`, `except` and `finally`**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as else, finally will execute regardless of `try` and `except` conditions

#### Dealing with files
- First iteration
```
 file = open("order.text") # open() takes a string arg with file name
 print(file) # Let's see the outcome and record it. File not found error will appear.
```
- Second iteration
```
try:
     file = open("order.text")
     print("File found") # Try block required except or will throw an error
 except FileNotFoundError as errmsg: # Creating alias same as a nickname
     print(f"File not found {errmsg}")
 finally: # Finally will execute regardless of try and except block execution, also used to clean up the code
     print("Thank you for visiting, see you again!")
```
#### Task - Create a function, Apply OOP and Create a package
- Step 1: Create a directory `FileFinder` and place the code for the task in there `file_handling_task.py`
```
class FileFind:
    def file_find(self, name):
        try:
             file = open(name)
             print("File found")
        except FileNotFoundError as errmsg:
             print(f"File not found {errmsg}")
        finally:
             print("Thank you for visiting!")
```
- Step 2: Create __init__.py in the directory
- Step 3: Create setup.py
```
from setuptools import setup

setup(name="Find File")
version = "1.00"
description = "File app"
author = "Saim at Sparta"
author_email = "saim22r@gmail.com"
url = "http//:spartagloba.com"
```
- Step 4: Create program.py 
```
from FileFinder.file_handling_task import FileFind

file = FileFind()
file_name = input("What file would you like to open? ")
print(file.file_find(file_name))
```