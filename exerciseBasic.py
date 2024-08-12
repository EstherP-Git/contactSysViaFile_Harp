# Exercise: Python Part 4 - Loops, Lists, Functions, and More

# Instructions:
# 1. Import the turtle module for graphical representations.
# 2. Define a function called `draw_flower` that uses the turtle module to draw a flower pattern.
# 3. Inside `draw_flower`, set the turtle speed and use a loop to draw the flower petals.
# 4. Define a function called `print_list_elements` that takes a list as an argument and prints each element.
# 5. Define a function called `add_numbers` that takes two parameters with default values and returns their sum.
# 6. Create a dictionary with keys "name", "age", and "city" and assign them appropriate values.
# 7. Print the values of the dictionary using their keys.
# 8. Import the math module and use it to print the square root of 16.
# 9. Create a string and demonstrate using the `upper` and `lower` methods.
# 10. Import the os module and get the current working directory.
# 11. List all files in the current working directory and print them.
# 12. Define a function called `rename_files` that takes a folder path, removes prefixes "00_" and "01_" from filenames, and renames the files.

# 1. Import the turtle module for graphical representations.
import turtle

# 2. Define a function called `draw_flower` that uses the turtle module to draw a flower pattern.
def draw_flower():
    # 3. Inside `draw_flower`, set the turtle speed and use a loop to draw the flower petals.
    turtle.speed(10)
    for i in range(36):
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)
        turtle.right(10)
    turtle.done()

# 4. Define a function called `print_list_elements` that takes a list as an argument and prints each element.
def print_list_elements(my_list):
    for element in my_list:
        print(element)

# 5. Define a function called `add_numbers` that takes two parameters with default values and returns their sum.
def add_numbers(a=1, b=1):
    return a + b

# 6. Create a dictionary with keys "name", "age", and "city" and assign them appropriate values.
my_dict = {
    "name": "",
    "age": 25,
    "city": "New York"
}

# 7. Print the values of the dictionary using their keys.
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict['age']}")
print(f"City: {my_dict['city']}")

# 8. Import the math module and use it to print the square root of 16.
import math
print(f"The square root of 16 is: {math.sqrt(16)}")

# 9. Create a string and demonstrate using the `upper` and `lower` methods.
my_string = "Hello, World!"
print(f"Uppercase: {my_string.upper()}")
print(f"Lowercase: {my_string.lower()}")

# 10. Import the os module and get the current working directory.
import os

# 11. List all files in the current working directory and print them.
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")
files = os.listdir(current_directory)
print("Files in the current directory:")
for file in files:
    print(file)

# 12. Define a function called `rename_files` that takes a folder path, removes prefixes "00_" and "01_" from filenames, and renames the files.
def rename_files(folder):
    for filename in os.listdir(folder):
        if filename.startswith("00_") or filename.startswith("01_"):
            new_name = filename[3:]
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print("Files have been renamed.")

# Calling the functions to demonstrate their functionality
draw_flower()  # Draw a flower with turtle graphics
print_list_elements([1, 2, 3, 4, 5])  # Print elements of a list
print(f"Sum of 3 and 5 is: {add_numbers(3, 5)}")  # Add two numbers and print the result
rename_files(current_directory)  # Rename files in the current directory
