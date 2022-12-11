if __name__ == '__main__':
    res = []
    n = int(input())
    for nums in range(1, n+1):
        res.append(str(nums))
    print("".join(res))