S = input().strip()
count = 0
n = len(S)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if j - i == k - j:
                if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    count += 1
print(count)