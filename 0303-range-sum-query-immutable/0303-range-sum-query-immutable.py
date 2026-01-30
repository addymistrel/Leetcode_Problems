class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixArr = [nums[0]]
        for k in nums[1:]:
            self.prefixArr.append(self.prefixArr[-1] + k)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixArr[right]
        return self.prefixArr[right] - self.prefixArr[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)