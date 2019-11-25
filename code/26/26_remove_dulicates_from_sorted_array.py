class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for item in nums:
            if nums[i] != item:
                i +=1
                nums[i] = item
        return i+1
