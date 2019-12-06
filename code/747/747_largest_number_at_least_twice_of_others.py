class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxNum = max(nums)
        for i in range(n):
            item = nums[i]
            if maxNum < 2*item and maxNum !=item :
                return -1
        return nums.index(maxNum)