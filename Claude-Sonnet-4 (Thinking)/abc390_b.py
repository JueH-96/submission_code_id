N = int(input())
A = list(map(int, input().split()))

is_geometric = True
for i in range(1, N-1):
    if A[i] * A[i] != A[i-1] * A[i+1]:
        is_geometric = False
        break

print("Yes" if is_geometric else "No")