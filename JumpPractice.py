import math


def jumpSearch(arr, num, lengthOfArr):
    prev = 0
    step = math.sqrt(num)

    while(arr[int(min(step,lengthOfArr))-1]) < num:

        for

        prev = step;
        step = math.sqrt(arr[])




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