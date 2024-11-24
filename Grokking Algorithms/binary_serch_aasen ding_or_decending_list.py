def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    # Determine if the list is ascending or descending
    is_ascending = arr[low] < arr[high]
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == item:
            return mid
        
        if is_ascending:
            # Ascending order logic
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Descending order logic
            if guess > item:
                low = mid + 1
            else:
                high = mid - 1
    
    return None

# Test the function
ascending_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
descending_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(binary_search(ascending_list, 3))  # Output: 2
print(binary_search(descending_list, 3))  # Output: 6
print(binary_search(ascending_list, 5))  # Output: None
print(binary_search(descending_list, 1))  # Output: None
