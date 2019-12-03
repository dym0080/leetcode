class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r= [x.lower() for x in filter(str.isalnum, str(s))]
        return r == r[::-1]