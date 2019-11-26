class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for item in nums:
            try:
                s.remove(item)
            except:
                s.add(item)
        return s.pop()
    