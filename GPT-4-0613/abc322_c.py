import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = [0] + A + [N+1]
for i in range(1, N+1):
    idx = bisect.bisect_left(A, i)
    print(A[idx] - i)