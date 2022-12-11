import math


def jumpSearch(arr, numToFind, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n) - 1)] < numToFind:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < numToFind:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == numToFind:
        return prev

    return -1


# Driver code to test function
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 55
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number", x, "is at index", "%.0f" % index)

# This code is contributed by "Sharad_Bhardwaj".
