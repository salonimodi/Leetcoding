def uniquePaths(m: int, n: int) -> int:
    # Initialize the first row and column to 1
    # Since the combination for
    # dp[i][0] = dp[i-1][0]
    # dp[0][j] = dp[0][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # df_table = [[1]*n] + [[1] + [0]*(n-1) ] * (m-1)
    # Since dp[i][j] only depends on the calculated cells before,
    # we can simply initialize the value of all cells to 1.
    dp = [[1] * n] * m

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            print(dp[r][c])

    print(dp[-1][-1])


uniquePaths(2, 2)
