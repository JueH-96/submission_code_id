def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if n % 2 == 1 or k != n // 2:
            print("Yes")
        else:
            print("No")

solve()