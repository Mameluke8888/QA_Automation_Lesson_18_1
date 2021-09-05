# Exercise #2
# Create a program that will return how many digits are in a positive number using recursion.
# Test it with number 8, 89, 891
# Hint: We can determine how many digits a positive integer has by repeatedly dividing by 10
# (without keeping the remainder) until the number is less than 10, consisting of only 1 digit.

def recursive_digits(number):
    if number < 10:
        return 1
    else:
        return recursive_digits(number//10) + 1


n = int(input("Please enter positive integer number: "))
print("Number of digits: {}".format(recursive_digits(n)))
