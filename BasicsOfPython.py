import math

a = 3
b = 9
c = 'abc'
d = 're'

# Simple concatenation
print(a + b)
print(c + d)
print(c + str(a))

# float precession and formatting
print('this is string concat example {} {}'.format('with numbers', a))
print("{0:.3f}".format(a))
print('%.2f' % a)
print(round(23.54422, 2))

# use of math module
print(math.ceil(3.6))
print(math.floor(3.4))
print('%.2f' % (math.sqrt(2)))

# getting fractional value from floating number
ar = 2.5.as_integer_ratio()
print(type(ar))  # tuple
print(ar)   # (5, 2)
print(ar[0])    # 5

# Convert String float to float list in Python
test_str = "3.44, 7.8, 9.12, 100.2, 6.50"
listVal = [float(idx) for idx in test_str.split(', ')]
print(listVal)

anotherWay = list(map(float, test_str.split(', ')))
print(anotherWay)

# Convert List of String List to String List
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]
print(str(test_list))
print([''.join(val) for val in test_list])
# another way using map function
print(list(map(''.join, test_list)))

test_list_nums = ["[1, 4]", "[5, 6]", "[7, 10]"]
print([''.join(str(b) for b in eval(a)) for i, a in enumerate(test_list_nums)])
print(eval('[1, 4]'))  # one for to convert "[1, 4]" to [1, 4]
print(''.join(["1", "4"]))  # another for loop to make its element to str and concatenate

# convert String to a List

# case 1
givenStr = "Geeks for Geeks"
print(list(givenStr.split(' ')))

# case 2
anotherStr = "Saloni"
print([a for a in anotherStr])

# case 3
list1 = []
list1[:0] = anotherStr
print(list1)

# case 4
import re

print(re.findall('[a-z, A-Z]', 'Saloni'))

# case 5
import json

stringA = '["geeks", 2,"for", 4, "geeks",3]'
print(json.loads(stringA))

# case 6
import ast

print(ast.literal_eval(stringA))

# case 7
print(list(filter(lambda x: x in 'saloni', 'saloni')))

# case 8
print(list(map(str, 'saloni')))

# case 9
print(list("saloni"))
