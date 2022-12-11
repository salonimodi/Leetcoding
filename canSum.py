def canSum(target, nums, memo={}) -> bool:
    if target in memo:
        return memo[target]
    if target is 0:
        return True
    if target < 0:
        return False
    for n in nums:
        remainder = target - n
        if canSum(remainder, nums, memo):
            memo[remainder] = True
            return True
    memo[target] = False
    return False


if __name__ == "__main__":
    print("Hi There!!")
    print(canSum(13231, [2, 3, 5]))
