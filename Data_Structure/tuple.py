# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
def print_4th_elements():
    my_tuple = (5, 10, 15, 20, 25, 30, 35, 40)    
    print("4th element from start:", my_tuple[3])     
    print("4th element from end:", my_tuple[-4])


# 2. Write a program to check whether an element exists in a tuple or not.
def check_element_in_tuple():
    my_tuple = ('apple', 'banana', 'cherry')
    element = 'banana'
    if element in my_tuple:
        print(f"{element} exists ")
    else:
        print(f"{element} does not exist ")

# 3. Write a program to convert a list into a tuple.
def list_to_tuple():
    my_list = [1, 2, 3, 4, 5]
    my_tuple = tuple(my_list)
    return my_tuple


# 4. Write a program to find the index of an item in a tuple.
def find_index_in_tuple():
    my_tuple = ('a', 'b', 'c', 'd', 'e')
    item = 'c'
    for i in my_tuple:

        if i == item:
            index = my_tuple.index(i)
            print(f"Index of {item}: {index}")

# 5. Write a program to replace last value of tuples in a list to 100.  

def replace_last_value_in_tuples():
    my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    updated_list = [t[:-1] + (100,) for t in my_list]
    print("Updated list of tuples:", updated_list)



