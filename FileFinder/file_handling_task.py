class FileFind:

    def file_find(self, name):
        try:
             file = open(name)
             print("File found")
        except FileNotFoundError as errmsg:
             print(f"File not found {errmsg}")
        finally:
             print("Thank you for visiting!")

