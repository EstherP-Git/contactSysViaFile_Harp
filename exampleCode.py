my_lists = [1, 2, 3, 4]

# Function to print elements of a list
def print_list_elements(my_list):
    # Loop over each element in the list and print it
    for element in my_list:
        print("element",element)

print_list_elements(my_lists)
# Function to add two numbers with default parameters
def add_numbers(a=1, b=1):
    return a + b  # Return the sum of a and b

# Demonstrating the use of a dictionary
my_dict = {
    "name": "Andy",
    "age": 25,
    "city": "New York"
}

# Accessing values from the dictionary
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict['age']}")
print(f"City: {my_dict['city']}")

# Using the imported math module to perform square root calculation
import math
print(f"The square root of 16 is: {math.sqrt(16)}")

# Demonstrating string methods
my_string = "Hello, World!"
print(f"Uppercase: {my_string.upper()}")  # Convert to uppercase
print(f"Lowercase: {my_string.lower()}")  # Convert to lowercase

# Working with file system (using os module)
import os

# Getting the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Listing files in the current directory
files = os.listdir(current_directory)
print("Files in the current directory:")
for file in files:
    print(file)

# Function to rename files by removing a prefix
def rename_files(folder):
    for filename in os.listdir(folder):
        if filename.startswith("00_") or filename.startswith("01_"):
            new_name = filename[3:]  # Remove the first 3 characters
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print("Files have been renamed.")

# Calling the functions to demonstrate their functionality

print_list_elements([1, 2, 3, 4, 5])  # Print elements of a list
print(f"Sum of 3 and 5 is: {add_numbers(3, 5)}")  # Add two numbers and print the result
rename_files(current_directory)  # Rename files in the current directory
