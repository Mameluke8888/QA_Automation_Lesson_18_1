# Exercise #1
# Using recursion create a program that calculates the sum of a list of the numbers.

def recursive_sum(list_of_numbers):
    n = len(list_of_numbers)
    # print(n)
    # print(list_of_numbers)
    if n == 1:
        return list_of_numbers[0]
    elif n > 1:
        return recursive_sum(list_of_numbers[:-1]) + list_of_numbers[-1]
    else:
        print('List must have at least one element')


# numbers = [5, 1, -4, 19, 0, -1]

n = int(input("How many elements would you like in the list? "))
numbers = list(int(num) for num in input("Type all of the elements separated by space ").strip().split())
print()
print("List: ", numbers)
print()
print("Sum of all of the elements calculated by sum() function: {}".format(sum(numbers)))
print("Sum of all of the elements calculated by recursion: {}".format(recursive_sum(numbers)))

