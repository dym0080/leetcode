class Solution:
    def pivotIndex(self, nums)
        S = sum(nums)
        leftSum = 0
        for i,v in enumerate(nums):
            if leftSum == (S - leftSum -v):
                return i
            leftSum +=v
        return -1