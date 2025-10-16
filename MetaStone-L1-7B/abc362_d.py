import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    A = [0] + A  # 1-based indexing
    
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        adj[u].append((v, b))
        adj[v].append((u, b))
    
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = A[1]
    
    heap = []
    heapq.heappush(heap, (dist[1], 1))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, b in adj[u]:
            new_dist = current_dist + b + A[v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    output = []
    for i in range(2, N+1):
        output.append(str(dist[i]))
    print(' '.join(output))

if __name__ == '__main__':
    main()