def duplicate_zeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()  # Видаляємо останній елемент
            i += 1  # Інкрементуємо індекс, щоб уникнути безкінечного циклу
        i += 1

# Приклад використання:
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)  # Виведе [1, 0, 0, 2, 3, 0, 0, 4]

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2)  # Виведе [1, 2, 3]
