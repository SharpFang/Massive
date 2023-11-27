def sort_array_by_parity(nums):
    # Використовуємо вбудовану функцію sorted і ключ для сортування за парністю
    return sorted(nums, key=lambda x: x % 2)

# Приклад використання:
nums1 = [3, 1, 2, 4]
result1 = sort_array_by_parity(nums1)
print(result1)  # Виведе будь-який прийнятний варіант, наприклад, [2, 4, 3, 1]

nums2 = [0]
result2 = sort_array_by_parity(nums2)
print(result2)  # Виведе [0]
