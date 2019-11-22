# 方案1：
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,v in enumerate(nums):
            other = target -v
            arr =list(nums)
            del arr[i]
            if arr.count(other):
                return [i,arr.index(other)+1]


# 方案2：

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,v in enumerate(nums):
            other = target -v
            
            for key,value in d.items():
                if other == value:
                    return [i,key]
            d[i] = v
        return None