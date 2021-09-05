# Exercise #3
# Write a Python program to get the factorial of a non-negative integer.
#
# Hint: Factorial is the product of all positive integers less than or equal to n:
#


def recursive_factorial(number):
    if number < 1:
        return 1
    else:
        return number * recursive_factorial(number-1)


n = int(input("Please enter non-negative integer number: "))
print("Factorial: {}".format(recursive_factorial(n)))
