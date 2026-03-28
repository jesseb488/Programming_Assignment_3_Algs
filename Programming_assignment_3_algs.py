def read_input():
    k = int(input())

    values = {}
    for i in range(k):
        char, val = input().split()
        values[char] = int(val)

    A = input()
    B = input()

    return values, A, B

def initialize_dp(n, m):
    dp = []
    for i in range(n+1):
        row = []
        for j in range(m + 1):
            row.append(0)
        dp.append(row)
    return dp

def fill_dp(dp, A, B, values):
    n = len(A)
    m = len(B)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1] == B[j-1]:
                match_value = dp[i-1][j-1] + values[A[i-1]]
                if dp[i-1][j] > dp[i][j-1]:
                    best_without_match = dp[i-1][j]
                else:
                    best_without_match = dp[i][j-1]
                if match_value > best_without_match:
                    dp[i][j] = match_value
                else:
                    dp[i][j] = best_without_match

            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]


       

def main():
    values, A, B = read_input()

    n = len(A)
    m = len(B)

    dp = initialize_dp(n ,m)
    fill_dp(dp, A, B, values)
    print(dp[n][m])




if __name__ == "__main__":
    main()