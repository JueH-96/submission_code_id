n = int(input())
strings = [input().strip() for _ in range(n)]
strings.sort(key=lambda x: len(x))
print(''.join(strings))