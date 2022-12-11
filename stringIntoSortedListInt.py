Input = ['21', '1', '131', '12', '15']

# case 1
print(sorted([int(v) for v in Input]))

# case 2
print(sorted(list(map(int, Input)), reverse=True))

# case 3
list1 = [int(v) for v in Input]
list1.sort()
print(list1)

# case 4
print([int(a) for idx, a in enumerate(Input)])
