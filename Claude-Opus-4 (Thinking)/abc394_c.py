# YOUR CODE HERE
S = input().strip()

while "WA" in S:
    S = S.replace("WA", "AC", 1)

print(S)