strings = []
for _ in range(12):
    s = input()
    strings.append(s)

count = 0
for i in range(12):
    if len(strings[i]) == i + 1:
        count += 1

print(count)