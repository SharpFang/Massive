def valid_mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False
    
    peak_found = False
    peak_index = 0
    
    # Знаходимо підйом
    while peak_index < n - 1 and arr[peak_index] < arr[peak_index + 1]:
        peak_index += 1
    
    # Перевіряємо, чи є підйом
    if peak_index == 0 or peak_index == n - 1:
        return False
    
    # Перевіряємо, чи є спадання
    while peak_index < n - 1 and arr[peak_index] > arr[peak_index + 1]:
        peak_index += 1
        peak_found = True
    
    return peak_found and peak_index == n - 1

# Приклад використання:
arr1 = [2, 1]
result1 = valid_mountain_array(arr1)
print(result1)  # Виведе False

arr2 = [3, 5, 5]
result2 = valid_mountain_array(arr2)
print(result2)  # Виведе False

arr3 = [0, 3, 2, 1]
result3 = valid_mountain_array(arr3)
print(result3)  # Виведе True
