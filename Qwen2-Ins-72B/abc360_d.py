import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '
'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, T = map(int, input().split())
    S = input().rstrip()
    X = list(map(int, input().split()))
    uf = UnionFind(N)
    for i in range(N):
        if S[i] == '0':
            X[i] -= T
        else:
            X[i] += T
    X = sorted([(x, i) for i, x in enumerate(X)])
    for i in range(N-1):
        if X[i][0] + T >= X[i+1][0] - T:
            uf.union(X[i][1], X[i+1][1])
    ans = 0
    for i in range(N):
        if S[i] == '0':
            for j in range(i+1, N):
                if S[j] == '1':
                    if uf.same(i, j):
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()