
# 1. Write a program to remove a given item from the set.
def remove_item_from_set():
    my_set = {1, 2, 3, 4, 5}
    item = 3

    if item in my_set:
        my_set.remove(item)

    print("Set after removing item:", my_set)

# 2. Write a program to create an intersection of sets.
def intersection_of_sets():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = set()

    for item in set1:
        if item in set2:
            result.add(item)

    print("Intersection of sets:", result)

# 3. Write a program to create a union of sets.
def union_of_sets():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    result = set()

    for item in set1:
        result.add(item)

    for item in set2:
        result.add(item)

    print("Union of sets:", result)

# 4. Write a program to find the maximum and minimum value in a set.
def max_min_in_set():
    my_set = {10, 20, 5, 30}

    max_value = None
    min_value = None

    for item in my_set:
        if max_value is None or item > max_value:
            max_value = item
        if min_value is None or item < min_value:
            min_value = item

    print("Maximum value:", max_value)
    print("Minimum value:", min_value)
