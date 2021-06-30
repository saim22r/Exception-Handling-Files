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