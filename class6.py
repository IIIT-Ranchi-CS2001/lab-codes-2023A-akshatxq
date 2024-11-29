#PROBLEM 1:-
def my_zip(names, ids, points, strct=False):
    if strct and not (len(names) == len(ids) == len(points)):
        return []  # Return empty list if lengths are not equal and strct is True
    
    min_length = min(len(names), len(ids), len(points))
    return list(zip(names[:min_length], ids[:min_length], points[:min_length]))

names = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103]
points = [1200, 1500, 1300]
# strct = True (checks if lists have equal length)
result_strct_true = my_zip(names, ids, points, strct=True)
print(result_strct_true)
# strct = False (zips using the minimum length)
result_strct_false = my_zip(names, ids, points, strct=False)
print(result_strct_false)

#PROBLEM 2:-
def my_sort(data, key):
    # Bubble Sort implementation
    n = len(data)
    # Perform sorting based on the 'key' value
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare based on the specified key
            if key == 0:  # Sort by customer name
                if data[j][0] > data[j + 1][0]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif key == 1:  # Sort by customer ID
                if data[j][1] > data[j + 1][1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif key == 2:  # Sort by shopping points
                if data[j][2] > data[j + 1][2]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

names = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103]
points = [1200, 1500, 1300]
# Create list of tuples using my_zip (assuming my_zip is defined as before)
customer_data = my_zip(names, ids, points, strct=False)
# Sort by customer name (key=0)
sorted_by_name = my_sort(customer_data, key=0)
print(sorted_by_name)
# Sort by customer ID (key=1)
sorted_by_id = my_sort(customer_data, key=1)
print(sorted_by_id)
# Sort by shopping points (key=2)
sorted_by_points = my_sort(customer_data, key=2)
print(sorted_by_points)

#PROBLEM 3:-
def my_max(container):
    # Ensure the container is not empty
    if not container:
        raise ValueError("The container is empty, cannot find maximum.")
    # Initialize the first element as the current maximum
    max_value = container[0]
    # Iterate over the container and find the maximum value
    for item in container:
        if item > max_value:
            max_value = item

    return max_value
numbers_list = [1, 3, 5, 7, 2]
print("Max in list:", my_max(numbers_list))
# Set example
numbers_set = {1, 3, 5, 7, 2}
print("Max in set:", my_max(numbers_set))
# Tuple example
numbers_tuple = (1, 3, 5, 7, 2)
print("Max in tuple:", my_max(numbers_tuple))

#PROBLEM 4:-
import re

# Function to extract and process the input string
def process_string(input_string):
    # Remove extra spaces and split the string by commas
    input_list = input_string.split(',')
    
    # Task 1: Find all letters and convert them to uppercase
    letters = filter(lambda x: x.isalpha(), ''.join(input_list))  # Filter all alphabet characters
    uppercase_letters = map(lambda x: x.upper(), letters)  # Convert them to uppercase
    print("Letters in uppercase:", list(uppercase_letters))
    
    # Task 2: Find all digits and calculate their squares
    digits = filter(lambda x: x.isdigit(), ''.join(input_list))  # Filter all digits
    digit_squares = map(lambda x: int(x)**2, digits)  # Square each digit
    print("Squares of digits:", list(digit_squares))
    
    # Task 3: Display all alphanumeric characters (letters + digits)
    alphanumeric = filter(lambda x: x.isalnum(), ''.join(input_list))  # Filter alphanumeric characters
    print("Alphanumeric characters:", list(alphanumeric))

user_input = input("Enter a comma-separated string: ")
process_string(user_input)
