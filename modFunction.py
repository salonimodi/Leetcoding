# # rear = -1
# # maxSize = 3  # 0, 1, 2
# # for i in range(3):
# #     rear = (1 + rear) % maxSize
# #     print(rear)
# print(ord('a'))
# print(ord('a') % 3)
# print(ord('b') % 3)
# print(ord('c') % 3)
# expected = 'a'
# print(chr(ord('a') + (ord(expected) % 3)))

str = 'aabccb'
count = 0
expected = 'a'
for c in str:
    if c != expected:
        while c != expected:
            expected = chr(ord('a') + ord(expected) % 3)
            count += 1
    expected = chr(ord('a') + ord(expected) % 3)
print(count)
