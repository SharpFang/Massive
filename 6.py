def remove_duplicates(nums):
    if not nums:
        return 0

    unique_count = 1  # Початкова кількість унікальних елементів
    current = nums[0]  # Поточний унікальний елемент

    for num in nums[1:]:
        if num != current:
            current = num
            nums[unique_count] = num
            unique_count += 1

    return unique_count

# Приклад використання:
nums1 = [1, 1, 2]
result1 = remove_duplicates(nums1)
print(result1, nums1[:result1])  # Виведе 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = remove_duplicates(nums2)
print(result2, nums2[:result2])  # Виведе 5, [0, 1, 2, 3, 4]
