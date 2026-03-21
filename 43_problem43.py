'''
Write a function that takes a filename as input and returns True if the file exists and False otherwise.
'''


import os

def check_file_exists(filename):
    return os.path.exists(filename)

# Example usage:
filename = "sample.txt"
exists = check_file_exists(filename)
print(f"Does '{filename}' exist? {exists}")