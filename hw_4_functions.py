"""
Homework for lesson 4. Functions and pretty code
"""


def largest_of_two_numbers(num1: float = 0, num2: float = 0) -> float:
    """Compare two numbers and return the largest."""
    if num1 > num2:
        result = num1
    else:
        result = num2
    return float(result)


def smallest_of_three_numbers(num1: float = 0, num2: float = 0, num3: float = 0) -> float:
    """Compare three numbers and return the smallest."""
    if num1 < num2 and num1 < num3:
        result = num1
    elif num2 < num1 and num2 < num3:
        result = num2
    else:
        result = num3
    return result


def abs_of_number(num: float = 0) -> float:
    """Return the absolute value of the number."""
    if num < 0:
        num = - num
    return num


def sum_of_two_numbers(num1: float = 0, num2: float = 0) -> float:
    """Print the sum of two numbers."""
    print(f"The sum of 1st and 2nd numbers is {num1 + num2}")


def number_sign(num: float = 0):
    """Print the sign of the number."""
    if num < 0:
        print(f"Number {num} is negative")
    elif num > 0:
        print(f"Number {num} is positive")
    else:
        print("It's zero")


# check functions
number_first = float(input("Enter 1st number: ", ))
number_second = float(input("Enter 2nd number: ", ))
number_third = float(input("Enter 3rd number: ", ))
print("-" * 20 + "FUNCTION 1" + "-"*20)
print(f"The largest of 1st and 2nd numbers is "
      f"{largest_of_two_numbers(number_first, number_second)}")
print("-" * 20 + "FUNCTION 2" + "-"*20)
print(f"The smallest of three numbers is "
      f"{smallest_of_three_numbers(number_first, number_second, number_third)}")
print("-" * 20 + "FUNCTION 3" + "-"*20)
print(f"The absolute value of first number is "
      f"{abs_of_number(number_first)}")
print("-" * 20 + "FUNCTION 4" + "-"*20)
sum_of_two_numbers(number_first, number_second)
print("-" * 20 + "FUNCTION 5" + "-"*20)
number_sign(number_first)
