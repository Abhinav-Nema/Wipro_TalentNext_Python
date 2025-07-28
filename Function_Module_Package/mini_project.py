

'''
MINI PROJECT 1

Write a Python functionthat accepts a hyphen-separated sequence of colorsas input and returnsthe colorsin a hyphen-separated sequence after sorting them alphabetically.
Constraint: 
  All the colors will be completely in either lower case or upper case.
    Sample 
    input1:green-red-yellow-black-whiteSample 
    output1:black-green-red-white-yellow
'''

def sort_colors(color_string):
    
    color_list = color_string.split('-')

 
    color_list.sort()

    sorted_colors = '-'.join(color_list)

    return sorted_colors


# Testing the function with sample inputs
input1 = "green-red-yellow-black-white"
print("Sample input 1:", input1)
print("Sample output 1:", sort_colors(input1))

input2 = "PINK-BLUE-TAN-PURPLE"
print("Sample input 2:", input2)
print("Sample output 2:", sort_colors(input2))


'''
MINI PROJECT 2

Create a Python module with the following functions:
Function NameTaskispalindrome(name) Given the user name as input, this function should tell us whether the name is a palindrome or not.

count_the_vowels(name)Given the user name as input, this function should tell us howmany vowels are present in it.

frequency_of_letters(name)Given the user name as input, this function should tell us how many times each letter appears in the name.
'''

def ispalindrome(name):
    name = name.replace(" ", "") 
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    print("No of vowels:", count)


def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != " ":
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    print("Frequency of letters:")
    for key in sorted(freq.keys()):
        print(f"{key}-{freq[key]}", end=", ")
    
