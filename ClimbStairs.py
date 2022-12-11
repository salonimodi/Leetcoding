class LeetPractise:

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        stepCount = [1, 2]
        for i in range(2, n):
            stepCount.append(stepCount[i - 1] + stepCount[i - 2])

        print(stepCount)
        return stepCount[n-1]


if __name__ == "__main__":
    print("Hi There!!")
    l1 = LeetPractise()
    print(l1.climbStairs(10))
