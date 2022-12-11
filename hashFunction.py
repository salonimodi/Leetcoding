a = '1 2'
t = tuple(map(int, a.split(' ')))
print(hash(t))