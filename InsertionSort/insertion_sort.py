def isort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(isort(arr))  # [11, 12, 22, 25, 34, 64, 90]
