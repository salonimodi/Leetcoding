if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for idx in range(n):
        arr.append([])
        arr[idx].append(input().split())

    for i in range(len(arr)):
        print(arr[i])