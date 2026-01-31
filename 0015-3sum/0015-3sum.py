class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(set(nums)) == 1 and nums[0] == 0:
            return [[0, 0, 0]]

        ans = set()
        for i in range(len(nums)):
            visited = set()
            for j in range(i + 1, len(nums)):
                curr2Sum = nums[i] + nums[j]
                if -curr2Sum in visited:
                    ans.add(tuple(sorted([nums[i], nums[j], -curr2Sum])))
                visited.add(nums[j])
        return [list(t) for t in ans]