class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) <= len(nums2):
            for item in nums1:
                if item in nums2:
                    nums2.remove(item)
                    result.append(item)
            return result
        else:
            for item in nums2:
                if item in nums1:
                    nums1.remove(item)
                    result.append(item)
            return result