import heapq
import sys

read = sys.stdin.readline

n = int(read())
heap = []

for i in range(n):
    x = int(read())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
