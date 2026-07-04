class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greaterMap = {}
        for k in nums2:
            if k not in greaterMap:
                greaterMap[k] = -1
            while len(stack) > 0 and stack[-1] < k:
                greaterMap[stack.pop()] = k
            stack.append(k)
        return [greaterMap[k] for k in nums1]