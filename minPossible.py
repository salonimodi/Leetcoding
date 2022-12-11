if __name__ == '__main__':
    arr = [3, 2, 1, 2, 7]
    arr.sort()
    ans = []
    last_num = 0
    for i in range(len(arr)):
        ans += [max(last_num+1, arr[i])]
        last_num = ans[i]
    print(sum(ans))


