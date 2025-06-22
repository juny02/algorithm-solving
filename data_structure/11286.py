from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
N = int(input())

heap = []
nums = defaultdict(list)
result = []
for _ in range(N):
    num = int(input())
    if num == 0:
        try:
            key = heapq.heappop(heap)
            heapq.heapify(nums[key])
            result.append(heapq.heappop(nums[key]))
        except Exception:
            result.append(0)
    else:
        nums[abs(num)].append(num)
        heapq.heappush(heap, abs(num))

for r in result:
    print(r)

    """
    튜플넣으면 두번째꺼 기반으로도 정렬한대 너무어이없수..
    
    """