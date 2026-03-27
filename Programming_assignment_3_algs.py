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

def main():
    values, A, B = read_input()

    n = len(A)
    m = len(B)

    dp = initialize_dp(n ,m)

    #prints for testing
    print("Values: ", values)
    print("A:", A)
    print("B:", B)
    print("DP size:", n+1, "x", m+1)


if __name__ == "__main__":
    main()