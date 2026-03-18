import os

def check_file_exists(filename):
    return os.path.exists(filename)

# Example usage:
filename = "sample.txt"
exists = check_file_exists(filename)
print(f"Does '{filename}' exist? {exists}")