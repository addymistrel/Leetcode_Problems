from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}  # prefix sum -> frequency
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_count:
                count += prefix_count[curr_sum - k]
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return count
