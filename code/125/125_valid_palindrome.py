class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r= [x.lower() for x in filter(str.isalnum, str(s))]
        if r == r[::-1]:
            return True
        else:
            return False