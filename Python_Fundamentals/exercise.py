import math

'''
Q1. Write a program to check if a given number is Positive, Negative or Zero.

'''
def check_number(number):
    if number == 0:
        return "Zero"
    
    elif number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

'''
Q2. Write a program to check if a given number is odd or even.
'''     
def odd_even(number):
    if number%2 == 0:
        return "Even"
    else:
        return "Odd" 
    
'''
Q3. # Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
'''    
def same_last_digit(num1, num2):
    if num1%10 == num2%10:
        return True
    else:
        return False

'''
Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
'''    
def print_number():
    for i in range(1,11):
        print(i, end="\t")

'''
Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
'''
def print_even():
    for i in range(23,57):
        if i%2 == 0:
            print(i)



'''
Q6. Write a program to check if a given number is prime or not.
'''
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    else:
        return True    
    



'''
Q7. Write a program to print prime numbers between 10 and 99.
'''
def prime_between():
    for i in range(10,99):
        if is_prime(i):
            print(i)

'''
Q8. Write a program to print the sum of all the digits of a given number.
'''
def print_sum(num):
    sum = 0
    while num != 0:
        sum += num%10
        num //= 10
    print(sum)

'''
Q9. Write a program to reverse a given number and print.
'''    
def reverse(num):
    reverse_num = 0

    while num != 0:
        reverse_num = (reverse_num*10) + num%10
        num = num//10
    
    print(reverse_num)
    return reverse_num

'''
Q10. Write a program to find if the given number is palindrom or not.
'''    
def is_palindrome(num):
    if num < 0:
        print("Not Palindrome")
    elif num == reverse(num):
        print("Palindrome")
    else:
        print("Not Palindrome")     




