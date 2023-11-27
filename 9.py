def replace_with_right_maximum(arr):
    n = len(arr)
    
    if n == 1:
        return [-1]
    
    max_right = arr[n - 1]
    arr[n - 1] = -1
    
    for i in range(n - 2, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current)
    
    return arr

# Приклад використання:
arr1 = [17, 18, 5, 4, 6, 1]
result1 = replace_with_right_maximum(arr1)
print(result1)  # Виведе [18, 6, 6, 6, 1, -1]

arr2 = [400]
result2 = replace_with_right_maximum(arr2)
print(result2)  # Виведе [-1]
