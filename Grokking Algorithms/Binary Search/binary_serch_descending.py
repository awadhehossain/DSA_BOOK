def binary_search_desc(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess < item:  
            high = mid - 1
        else:
            low = mid + 1
    return None

# List must be a sorted list in descending order
my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(binary_search_desc(my_list, 3))  # Output: 6
print(binary_search_desc(my_list, 1))  # Output: None
