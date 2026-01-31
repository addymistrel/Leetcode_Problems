class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for index, value in enumerate(numbers):
            if target - value in dic:
                return [dic[target - value] + 1, index + 1]
            dic[value] = index
        return [-1, -1]