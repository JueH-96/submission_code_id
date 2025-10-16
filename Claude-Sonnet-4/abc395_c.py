# YOUR CODE HERE
n = int(input())
a = list(map(int, input().split()))

min_length = float('inf')

for i in range(n):
    seen = set()
    for j in range(i, n):
        if a[j] in seen:
            # Found a duplicate, this subarray from i to j is valid
            min_length = min(min_length, j - i + 1)
            break
        seen.add(a[j])

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)