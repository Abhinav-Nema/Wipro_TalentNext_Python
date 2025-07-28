# 1. Write a program to count the number of upper and lower case letters in a String.
def count_upper_lower():
    text = "Hello World"
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1

    print("Number of uppercase letters:", upper)
    print("Number of lowercase letters:", lower)

# 2. Write a program that will check whether a given String is Palindrome or not.
def check_palindrome():
    word = "madam"
    reverse_word = word[::-1]

    if word == reverse_word:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.
# If input is "Wipro" then output should be "WiWiWiWiWi".
def repeat_first_two_chars():
    word = "Wipro"
    n = len(word)
    first_two = word[0:2]
    result = ""

    for i in range(n):
        result = result + first_two

    print("Result:", result)

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged.
# If the input is "xHix", then output is "Hi".
def remove_edge_x():
    word = "xHix"

    if len(word) > 0 and word[0] == 'x':
        word = word[1:]

    if len(word) > 0 and word[-1] == 'x':
        word = word[:-1]

    print("Final string:", word)

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.
def repeat_last_n_chars():
    word = "Wipro"
    n = 3
    last_part = word[-n:]
    result = ""

    for i in range(n):
        result = result + last_part

    print("Result:", result)