'''
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.

'''
import os 

def list_directory_contents(path):
    try:
        for e, item in enumerate(os.listdir(path)):
            print(f"{e + 1}.", item)
    except PermissionError as pe:
        print(f"Permission Error: {pe}\nTriggered at {item}")
    except FileNotFoundError as fnf:
        print(f"File not found: no directory named {path}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


user_path = input("What path would you like to see all files and subdirectories for? ")
list_directory_contents(user_path)