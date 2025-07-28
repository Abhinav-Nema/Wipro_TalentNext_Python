# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
def display_list():
    my_list = [10, 20, 30, 40, 50]
    print("Full List:", my_list)
    for i in range(len(my_list)):
        print(f"Element at index {i} is {my_list[i]}")

# 2. Write a program to append a new item to the end of the list.
def append_item():
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    print(f"After appending list is {my_list}")

# 3. Write a program to reverse the order of the items in the list.
def reverse_list():
    my_list = [10, 20, 30, 40, 50]
    my_list.reverse()
    print(my_list)

# 4. Write a program to print the number of occurrences of a specified element in a list.
def count_occurrences():
    my_list = [1, 2, 2, 3, 2, 4, 5]
    element = 2
    count = my_list.count(element)
    print(f"Number of occurrences of {element}:{count}")

# 5. Write a program to append the items of list1 to list2 in the front.
def append_front():
    list1 = [4, 5, 6]
    list2 = [1, 2, 3]
    list2 = list1 + list2  # Appending list1 to the front of list2
    print("After appending in front:", list2)

# 6. Write a program to insert a new item before the second element in an existing list.
def insert_before_second():
    my_list = [10, 20, 30, 40]
    my_list.insert(1, 15)  # Index 1 is before the second element
    print(my_list)

# 7. Write a program to remove the item from a specified index in a list.
def remove_by_index():
    my_list = [10, 20, 30, 40, 50]
    index = 2
    removed = my_list.pop(index)
    print("List after removal:", my_list)
    
# 8. Write a program to remove the first occurrence of a specified element from a list.
def remove_first_occurrence():
    my_list = [1, 2, 3, 2, 4, 2]
    element = 2
    if element in my_list:
        my_list.remove(element)
        print(f"List after removing first occurrence of {element}:", my_list)
    else:
        print(f"{element} not found in list.")
