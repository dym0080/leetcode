import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashCount = collections.Counter(s)
        
        for item in s:
            if hashCount[item] == 1:
                return s.index(item)
        return -1
        