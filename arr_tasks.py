# Two sum
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []

print("Two sum")
print("Исходный массив: [3, 8, 9, 11, 16, 18, 19, 21]")
print(f"Результат: {twoSum([3, 8, 9, 11, 16, 18, 19, 21], 25)}")

# Развернуть массив
def reverseArray(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -= 1
    return arr

print("\nРазвернуть массив")
print("Исходный массив: [3, 8, 6, 9, 9, 8, 6]")
print(f"Результат: {reverseArray([3, 8, 6, 9, 9, 8, 6])}")

# Развернуть часть массива
def reverseArray(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -= 1

def solution(arr, k):
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, k % n - 1)
    reverseArray(arr, k % n, n - 1)
    return arr

print("\nРазвернуть часть массива")
print("""Исходные данные: [1, 2, 3, 4, 5, 6, 7]
k=3""")
print(f"Результат: {solution([1, 2, 3, 4, 5, 6, 7], 3)}")

# Слияние 2х сортированных массива
def merge(arr1, arr2):
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1
    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        pointer3 -= 1
    return arr1

print("\nСлияние 2х сортированных массива")
print("""Исходный массив: [3, 8, 10, 11, 0, 0, 0]
[1, 7, 9]""")
print(merge(
    [3, 8, 10, 11, 0, 0, 0],
    [1, 7, 9]
))

# Сортировка массива нулей и единиц
def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    return arr

print("\nСортировка массива нулей и единиц")
print("Исходный массив: [0, 1, 1, 0, 1, 0, 1, 0]")
print(f"Результат: {sort_binary_array([0, 1, 1, 0, 1, 0, 1, 0])}")

# Задача флага Нидерландов
def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print("\nЗадача флага Нидерландов")
print("Исходный массив: [2, 0, 2, 1, 1, 0]")
print(f"Результат: {sortColors([2, 0, 2, 1, 1, 0])}")

# Передвинуть чётные числа вперёд
def evenFirst(arr):
    evenIndex = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenIndex] = arr[evenIndex], arr[i]
            evenIndex += 1
    return arr

print("\nПередвинуть чётные числа вперёд")
print("Исходный массив: [3, 2, 4, 1, 11, 8, 9]")
print(f"Результат: {evenFirst([3, 2, 4, 1, 11, 8, 9])}")

# Передвинуть нули в конец
def zeroLast(arr):
    zeroIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[zeroIndex] = arr[zeroIndex], arr[i]
            zeroIndex += 1
    return arr

print("\nПередвинуть нули в конец")
print("Исходный массив: [0, 0, 1, 0, 3, 12]")
print(f"Результат: {zeroLast([0, 0, 1, 0, 3, 12])}")

print("Исходный массив: [0, 33, 57, 88, 60, 0, 0, 80, 99]")
print(f"Результат: {zeroLast([0, 33, 57, 88, 60, 0, 0, 80, 99])}")

print("Исходный массив: [0, 0, 0, 18, 16, 0, 0, 77, 99]")
print(f"Результат: {zeroLast([0, 0, 0, 18, 16, 0, 0, 77, 99])}")
