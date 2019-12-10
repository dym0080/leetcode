class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = "".join(str(x) for x in nums)
        return max(len(x) for x in a.split('0'))