def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  # Target is not in the list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 6

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the list.")
