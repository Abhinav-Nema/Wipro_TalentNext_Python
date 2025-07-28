# 1. Write a function to return the sum of all numbers in a list.  
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 2. Write a function to return the reverse of a string.  
def reverse_string(s):
    return s[::-1]


# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_upper_lower(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)


# 5. Write a function to print the even numbers from a given list. 
def print_even_numbers(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)


# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


