def max_ones_count(nums, index=0, current_count=0, max_count=0):
    # Базовий випадок: досягнуто кінця масиву
    if index == len(nums):
        return max_count
    
    # Збільшуємо поточну кількість 1-ць, якщо поточний елемент - 1
    if nums[index] == 1:
        current_count += 1
    else:
        # Скидаємо лічильник, якщо зустріли 0
        current_count = 0
    
    # Оновлюємо максимальну кількість
    max_count = max(max_count, current_count)
    
    # Рекурсивний виклик для наступного елемента
    return max_ones_count(nums, index + 1, current_count, max_count)

# Приклад використання:
nums1 = [1, 1, 0, 1, 1, 1]
result1 = max_ones_count(nums1)
print(result1)  # Виведе 3

nums2 = [1, 0, 1, 1, 0, 1]
result2 = max_ones_count(nums2)
print(result2)  # Виведе 2