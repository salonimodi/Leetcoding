# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
for i in range(T):
    flag = 1
    s = input()
    if not (len(re.findall(r'[A-Z]', s)) >= 2):
        flag = 0
    elif not (len(re.findall(r'[0-9]', s)) >= 3):
        flag = 0
    elif not (re.match(r'^[a-zA-Z0-9]{10}$', s)):
        flag = 0
    elif re.search(r'([a-zA-Z0-9]).*\1+', s):
        flag = 0

    print('Valid' if flag else 'Invalid')