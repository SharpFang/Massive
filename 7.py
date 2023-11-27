def check_double(arr):
    seen = set()

    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)

    return False

# Приклад використання:
arr1 = [10, 2, 5, 3]
result1 = check_double(arr1)
print(result1)  # Виведе True

arr2 = [3, 1, 7, 11]
result2 = check_double(arr2)
print(result2)  # Виведе False
