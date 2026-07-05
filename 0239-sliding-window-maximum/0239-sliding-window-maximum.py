import heapq as hq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        # Build first window
        for i in range(k):
            hq.heappush(heap, (-nums[i], i))

        ans = [-heap[0][0]]

        # Process remaining windows
        for i in range(k, len(nums)):
            hq.heappush(heap, (-nums[i], i))

            # Remove elements outside the current window
            while heap and heap[0][1] <= i - k:
                hq.heappop(heap)

            ans.append(-heap[0][0])

        return ans