class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strDigits = ''.join(str(i) for i in digits)
        tmp = int(strDigits)+1
        tmp2 = str(tmp)
        return [int(i) for i in tmp2]