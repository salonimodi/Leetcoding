a = [5, 6, 6, 5, 7, 4, 7, 6]
diff = 10**6
a.sort()
for j in range(len(a)-1, -1, -1):
    print("j " + str(j))
    print(a[j:])
    subArray1 = sum(a[j:])
    print("1: " + str(subArray1))
    subArray2 = sum(a) - subArray1
    print("2: " + str(subArray2))
    diff = min(diff, abs(subArray1 - subArray2))
    print(diff)
    print("_______________")
