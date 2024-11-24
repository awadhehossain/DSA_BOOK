def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
# List must be a sorted list 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_list, 3))  # Output: 2
print(binary_search(my_list, -1))  # Output: None
