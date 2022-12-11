from typing import List


class LeetPractise:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCost = [0]*len(cost)
        if len(cost) <= 1:
            return cost
        totalCost[1] = cost[1]
        totalCost[0] = cost[0]
        for i in range(2, len(cost)):
            totalCost[i] = cost[i] + min(totalCost[i-1], totalCost[i-2])
        return min(totalCost[-1], totalCost[-2])


if __name__ == "__main__":
    print("Hi There!!")
    l1 = LeetPractise()
    print(l1.minCostClimbingStairs([4, 5, 2, 10, 22]))
