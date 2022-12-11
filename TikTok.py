
if __name__ == '__main__':
    m = {}
    T = int(input())
    for _ in range(T):
        m[T] = set(input().split())

    for i in m:
        print(int(i)+":"+int(m[i]))



