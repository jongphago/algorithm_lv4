import heapq

N = 18
heap = []
total = 0
nums = nums = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]

for x in nums:
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            total += heapq.heappop(heap)[1]
        else:
            total += 0

print(total)