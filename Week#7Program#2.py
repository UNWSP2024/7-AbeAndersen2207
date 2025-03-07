#UNWSP Programming PythonCos2005DEsp25
#Week#7_Program#2 Larger than n
#03/7/2025
#Abraham. N. Andersen

#In a program, write a function (with NO output) that accepts two arguments: a list, and a number n.
#Assume that the list contains numbers.  The function should display all of the numbers in the list
#that are greater than then number n.

def find_larger_numbers(number_list, n):
    """
    Finds and displays numbers in a list that are greater than n.

    Args:
        number_list: A list of numbers (integers).
        n: A number (integer) to compare against.
    """
    for number in number_list:
        if number > n:
            print(number)

# Get input from the user
while True:
    try:
        numbers_input = input("Enter a list of whole numbers, separated by spaces: ")
        number_list = [int(num) for num in numbers_input.split()] #Changed float to int
        break
    except ValueError:
        print("Invalid input. Please enter whole numbers separated by spaces.")

while True:
    try:
        threshold = int(input("Enter a whole number to compare against: ")) #changed float to int.
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("Numbers greater than", threshold, "are:")
find_larger_numbers(number_list, threshold)