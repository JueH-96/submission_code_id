# YOUR CODE HERE
S = input()
n = len(S)
count = 0

for i in range(n):
    if S[i] == 'A':
        for j in range(i + 1, n):
            if S[j] == 'B':
                k = j + (j - i)
                if k < n and S[k] == 'C':
                    count += 1

print(count)